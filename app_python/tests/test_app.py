from app import app


def test_main_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health_page():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "healthy"


def test_404():
    client = app.test_client()
    response = client.get("/abracadabra")
    assert response.status_code == 404


def test_wrong_method():
    client = app.test_client()
    response = client.post("/health")
    assert response.status_code == 405