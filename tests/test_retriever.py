from src.retriever import Retriever

def test_retriever():
    ret = Retriever()
    results = ret.retrieve("credit card fees", top_k=3)
    assert len(results) == 3
    assert all('score' in r for r in results)
