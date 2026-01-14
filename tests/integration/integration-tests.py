import requests

BASE_URL = "http://localhost:8080"


def test_root_works():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200


def test_cats_page_works():
    r = requests.get(f"{BASE_URL}/cats")
    assert r.status_code == 200


def test_db_is_connected():
    r = requests.get(f"{BASE_URL}/")
    assert "cat" in r.text.lower() or "dog" in r.text.lower()
