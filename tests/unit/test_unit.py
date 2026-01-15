def test_cat_age_invalid(client):
    response = client.post("/cats/add", data={
        "name": "Kitty",
        "age": -5,  # invalid
        "arrival_date": "2024-01-01",
    })
    assert response.status_code == 400


def test_cat_not_found(client):
    response = client.get("/cats/999999")
    assert response.status_code == 404
