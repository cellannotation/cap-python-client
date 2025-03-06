import pytest
from unittest.mock import MagicMock, ANY
from cap_client import CapClient, MDSession
import pandas as pd


CAP_AUTHENTICATE_USER_URL  = "authenticate-user-wg6qkl5yea-uc.a.run.app"
CAP_AUTHENTICATE_TOKEN_URL = "authenticate-token-wg6qkl5yea-uc.a.run.app"

# ------------------------------
# Tests for CapClient methods
# ------------------------------

def test_search_datasets():
    cap = CapClient()

    df = cap.search_datasets(
        search="name",
        organism=["Homo sapiens"],
        tissue=["stomach"],
        assay=["10x 3' v1"],
        limit=10,
        offset=0,
        sort=[{"name": "ASC"}]
    )
    assert type(df) is pd.DataFrame, "Wrong response type!"


def test_search_cell_labels():
    cap = CapClient()

    df = cap.search_cell_labels(
        search="name",
        organism=["Homo sapiens"],
        tissue=["brain"],
        assay=["10x 3' v1"],
        limit=5,
        offset=0,
        sort=[{"name": "ASC"}]
    )
    assert type(df) is pd.DataFrame, "Wrong response type!"


def test_open_md_session():
    cap = CapClient()
    dataset_id = "1234"
    md_session = cap.md_session(dataset_id)
    assert isinstance(md_session, MDSession)
    assert md_session.dataset_id == dataset_id


# ------------------------------
# Tests for MDSession methods
# ------------------------------

@pytest.fixture
def dummy_md_session():
    """
    Returns an MDSession instance along with a dummy client (a MagicMock)
    so we can patch its methods.
    """
    dummy_client = MagicMock()
    md_session = MDSession(dataset_id="1234", _client=dummy_client)
    return md_session, dummy_client


@pytest.mark.parametrize("ready", [True, False])
def test_check_md_ready(ready, dummy_md_session):
    md_session, client = dummy_md_session
    dataset_mock = MagicMock()
    dataset_mock.is_embeddings_up_to_date = ready
    client.dataset_ready.return_value = MagicMock(dataset=dataset_mock)

    if ready:
        md_session._check_md_ready()
    else:
        with pytest.raises(RuntimeError):
            md_session._check_md_ready()


def test_create_session(dummy_md_session):
    md_session, dummy_client = dummy_md_session

    # Setup dummy response for dataset_ready (should be "ready")
    dummy_ready = MagicMock()
    dummy_ready.dataset = MagicMock(is_embeddings_up_to_date=True)
    dummy_client.dataset_ready.return_value = dummy_ready

    # Setup dummy response for dataset_initial_state_query
    dummy_initial_state = MagicMock()
    dummy_dataset = MagicMock()
    dummy_labelset = MagicMock()
    dummy_labelset.mode = "cell-labels"
    dummy_labelset.name = "Test Labelset"
    dummy_labelset.id = "label1"
    dummy_dataset.labelsets = [dummy_labelset]
    dummy_dataset.model_dump.return_value = dict(dummy_dataset)
    dummy_initial_state.dataset = dummy_dataset
    dummy_client.dataset_initial_state_query.return_value = dummy_initial_state

    # Setup dummy response for cluster_types
    dummy_cluster_types = MagicMock()
    dummy_cluster_dataset = MagicMock()
    dummy_cluster = MagicMock()
    dummy_cluster.name = "cluster1"
    dummy_cluster_dataset.embedding_cluster_types = [dummy_cluster]
    dummy_cluster_types.dataset = dummy_cluster_dataset
    dummy_client.cluster_types.return_value = dummy_cluster_types

    # Setup dummy response for md_commons_query (for embeddings)
    dummy_embeddings = MagicMock()
    dummy_embeddings_dataset = MagicMock()
    dummy_embedding = MagicMock()
    dummy_embedding.name = "embedding1"
    dummy_embeddings_dataset.embeddings = [dummy_embedding]
    dummy_embeddings.dataset = dummy_embeddings_dataset
    dummy_client.md_commons_query.return_value = dummy_embeddings

    # Setup dummy response for create_session
    dummy_create_session = MagicMock()
    dummy_create_session.save_embedding_session = "snapshot_updated"
    dummy_client.create_session.return_value = dummy_create_session

    session_id = md_session.create_session()

    # Check that the returned session_id matches the session property
    assert md_session.session_id == session_id

    # Verify that the expected internal client calls were made
    dummy_client.dataset_ready.assert_called_once_with(md_session.dataset_id)
    dummy_client.dataset_initial_state_query.assert_called_once_with(md_session.dataset_id)
    dummy_client.cluster_types.assert_called_once_with(md_session.dataset_id)
    dummy_client.md_commons_query.assert_called_once_with(md_session.dataset_id)
    dummy_client.create_session.assert_called_once()


def test_create_session_not_ready(dummy_md_session):
    md_session, dummy_client = dummy_md_session

    # Simulate dataset not ready (is_embeddings_up_to_date is False)
    dummy_ready = MagicMock()
    dummy_ready.dataset = MagicMock(is_embeddings_up_to_date=False)
    dummy_client.dataset_ready.return_value = dummy_ready

    with pytest.raises(RuntimeError, match="is not ready"):
        md_session.create_session()


def test_embedding_data_success(dummy_md_session):
    md_session, dummy_client = dummy_md_session
    # Set available embeddings so that "embedding1" is valid.
    md_session._embeddings = ["embedding1"]

    # Setup dummy response for embedding_data
    dummy_embedding_data = MagicMock()
    dummy_embedding_data.dataset = MagicMock(embedding_data="embedding_data_response")
    dummy_client.embedding_data.return_value = dummy_embedding_data

    result = md_session.embedding_data(
        embedding="embedding1",
        max_points=1000,
        labelsets=["label1"],
        selection_gene="geneA",
        selection_key_major="sel_major",
        selection_key_minor="sel_minor"
    )
    assert result == "embedding_data_response"
    dummy_client.embedding_data.assert_called_once_with(
        dataset_id=md_session.dataset_id,
        options=ANY  # We use ANY because the input options object is complex
    )


def test_embedding_data_invalid_embedding(dummy_md_session):
    md_session, dummy_client = dummy_md_session
    md_session._embeddings = ["embedding1"]

    with pytest.raises(ValueError, match="is not found"):
        md_session.embedding_data(
            embedding="nonexistent",
            max_points=1000
        )


def test_general_de_success(dummy_md_session):
    md_session, dummy_client = dummy_md_session
    # Set available labelsets so that "Test Label" is valid.
    md_session._labelsets = ["Test Label"]

    # Patch the internal helper to return a dummy labelset id.
    md_session._labelset_id_from_name = MagicMock(return_value="label1")

    dummy_general_de = MagicMock()
    dummy_general_de.dataset = MagicMock(general_diff="diff_key")
    dummy_client.general_de.return_value = dummy_general_de

    md_session._session_id = "session-id"
    result = md_session.general_de(labelset="Test Label", random_seed=42)
    assert result == "diff_key"
    md_session._labelset_id_from_name.assert_called_once_with("Test Label")
    dummy_client.general_de.assert_called_once_with(
        dataset_id=md_session.dataset_id,
        options=ANY
    )


def test_general_de_invalid_labelset(dummy_md_session):
    md_session, dummy_client = dummy_md_session
    md_session._labelsets = ["Test Label"]

    with pytest.raises(ValueError, match="is not found"):
        md_session.general_de(labelset="Nonexistent")


def test_highly_variable_genes(dummy_md_session):
    md_session, dummy_client = dummy_md_session

    # Setup dummy response for highly_variable_genes
    dummy_gene = MagicMock()
    dummy_gene.name = "gene1"
    dummy_gene.dispersion = 0.5
    dummy_hvg = MagicMock()
    dummy_hvg.dataset = MagicMock(embedding_highly_variable_genes=[dummy_gene])
    dummy_client.highly_variable_genes.return_value = dummy_hvg

    df = md_session.highly_variable_genes(
        gene_name_filter="g",
        pseudogenes_filter=True,
        offset=0,
        limit=10,
        sort_order="desc"
    )

    # Check that the returned DataFrame contains the expected columns and values.
    assert isinstance(df, pd.DataFrame)
    assert "gene_symbol" in df.columns
    assert "dispersion" in df.columns
    assert df.iloc[0]["gene_symbol"] == "gene1"
    assert df.iloc[0]["dispersion"] == 0.5

    dummy_client.highly_variable_genes.assert_called_once_with(
        dataset_id=md_session.dataset_id,
        options=ANY
    )


def test_is_md_cache_ready(dummy_md_session):
    md_session, dummy_client = dummy_md_session
    dummy_files_status = MagicMock()
    dummy_files_status.dataset = MagicMock(get_md_files_status="ready")
    dummy_client.files_status.return_value = dummy_files_status

    assert md_session.is_md_cache_ready() is True
    dummy_client.files_status.assert_called_once_with(md_session.dataset_id)


def test_heatmap(dummy_md_session):
    md_session, dummy_client = dummy_md_session
    # Assume that create_session was already called so session_id is set.
    md_session._session_id = "session123"

    dummy_heatmap = MagicMock()
    dummy_heatmap.dataset = MagicMock(embedding_diff_heat_map="heatmap_response")
    dummy_client.heatmap.return_value = dummy_heatmap

    result = md_session.heatmap(diff_key="diff_key", n_top_genes=3, max_cells_displayed=1000)
    assert result == "heatmap_response"
    dummy_client.heatmap.assert_called_once_with(
        dataset_id=md_session.dataset_id,
        options=ANY
    )