from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["Project Test"]

# def test_int_value():
#     response = client.get("/numbers/25")
#     assert response.status_code == 200
#     assert response.json()['num'] == {'num': 'Num is Int: 25'}

