from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
item = {"name": "a", "description": "a"}

def test_create_item():
    response = client.post("/items/", json=item)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "a"
    assert data["description"] == "a"

def test_list_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_item():
    new_item = client.post("/items/", json=item)
    item_id = new_item.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "a"
    assert data["description"] == "a"
