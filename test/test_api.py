from cap_sc_client import CapClient


def test_dataset_search():
    cp = CapClient()
    df = cp.search_datasets(offset=5, limit=5)
    assert df.shape[0] == 5

def test_label_search():
    cp = CapClient()
    df = cp.search_cell_labels(offset=5, limit=5)
    assert df.shape[0] == 5

def test_md_session():
    cp = CapClient()
    datasets = cp.search_datasets(limit=1)
    dataset_id = datasets["id"].to_list()[0]
    md_session = cp.md_session(dataset_id=dataset_id)
    md_session.create_session()
    assert md_session.session_id is not None
    assert len(md_session.embeddings) > 0
