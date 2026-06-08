import pytest

from cap_sc_client import CapClient


MD_DATASET_ID = "825"


@pytest.fixture(scope="module")
def cap_client():
    return CapClient()


@pytest.fixture(scope="module")
def md_session(cap_client):
    session = cap_client.md_session(dataset_id=MD_DATASET_ID)
    session.create_session()
    return session


def test_dataset_search(cap_client):
    df = cap_client.search_datasets(offset=5, limit=5)

    assert df.shape[0] == 5
    assert {"id", "project"}.issubset(df.columns)
    assert df["id"].notna().all()
    assert df["project"].notna().all()


def test_label_search(cap_client):
    df = cap_client.search_cell_labels(offset=5, limit=5)

    assert df.shape[0] == 5
    assert {"id", "name"}.issubset(df.columns)
    assert df["id"].notna().all()
    assert df["name"].notna().all()


def test_md_session_create_session(md_session):
    assert md_session.dataset_id == MD_DATASET_ID
    assert md_session.session_id is not None
    assert md_session.dataset_snapshot is not None
    assert isinstance(md_session.embeddings, list)
    assert isinstance(md_session.labelsets, list)
    assert len(md_session.embeddings) > 0
    assert len(md_session.labelsets) > 0


def test_embedding_data(md_session):
    assert md_session.embeddings

    emb_data = md_session.embedding_data(
        embedding=md_session.embeddings[0],
        max_points=5_000,
    )

    assert emb_data is not None
    assert len(emb_data.obs_ids) > 0
    assert len(emb_data.positions) == len(emb_data.obs_ids)
    assert isinstance(emb_data.in_selection_major, list)
    assert isinstance(emb_data.in_selection_minor, list)
    assert len(emb_data.annotations) >= 0


def test_md_cache_ready(md_session):
    assert isinstance(md_session.is_md_cache_ready(), bool)


def test_highly_variable_genes(md_session):
    df = md_session.highly_variable_genes(limit=10)

    assert df.shape[0] > 0
    assert {"gene_symbol", "dispersion"}.issubset(df.columns)
    assert df["gene_symbol"].notna().all()
    assert df["dispersion"].notna().all()


@pytest.fixture(scope="module")
def labelset_for_de(md_session):
    for labelset_name in md_session.labelsets:
        matching_labelsets = [
            labelset
            for labelset in md_session.dataset_snapshot.labelsets
            if labelset.name == labelset_name
        ]
        if len(matching_labelsets) != 1:
            continue

        labels_with_cells = sum(label.count > 1 for label in matching_labelsets[0].labels)
        if labels_with_cells > 1:
            return labelset_name

    pytest.skip("Dataset has no labelset with more than one populated label")


@pytest.fixture(scope="module")
def diff_key(md_session, labelset_for_de):
    key = md_session.general_de(labelset_for_de)
    assert key is not None
    return key


def test_general_de(diff_key):
    assert isinstance(diff_key, str)
    assert diff_key


def test_heatmap(md_session, diff_key):
    heatmap = md_session.heatmap(diff_key=diff_key)

    assert heatmap is not None
    assert len(heatmap.obs_ids) > 0
    assert len(heatmap.genes) > 0
    assert len(heatmap.scores) > 0
    assert len(heatmap.is_in_selections) == len(heatmap.obs_ids)
