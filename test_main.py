from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["Project Test"]

def test_int_value():
    response = client.get("/numbers/3500")
    assert response.status_code == 200
    assert response.json() == {'Input': 'Num is Int: 3500', 'Output': '3.5K'}

def test_negative_int_value():
    response = client.get("/numbers/-3500")
    assert response.status_code == 200
    assert response.json() == {'Input': 'Num is Int: -3500', 'Output': '-3.5K'}

def test_float_value():
    response = client.get("/numbers/3500.500")
    assert response.status_code == 200
    assert response.json() == {'Input': 'Num is Float: 3500.500', 'Output': '3.5K'}


def test_negative_float_value():
    response = client.get("/numbers/-35000.512345678")
    assert response.status_code == 200
    assert response.json() == {'Input': 'Num is Float: -35000.512345678', 'Output': '-35K'}
