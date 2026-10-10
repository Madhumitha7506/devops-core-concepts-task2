import app as app_module


def test_health():
    client = app_module.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data.strip() == b"ok"


def test_home_counts_views(monkeypatch):
    class FakeCache:
        def incr(self, key):
            return 7

    monkeypatch.setattr(app_module, "cache", FakeCache())
    client = app_module.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"7 times" in response.data
