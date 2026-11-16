from main import app


def client():
    return app.test_client()


def test_index():
    r = client().get("/")
    assert r.status_code == 200
    assert "host" in r.get_json()


def test_healthz():
    r = client().get("/healthz")
    assert r.get_json() == {"status": "ok"}


def test_metrics():
    client().get("/")
    r = client().get("/metrics")
    assert b"app_requests_total" in r.data
