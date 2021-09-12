from fastapi.testclient import TestClient

from fapi.main import app, some_function

client = TestClient(app)

def test_some_function():
    expected = "What do you want?"
    actual = some_function()
    assert expected == actual

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

