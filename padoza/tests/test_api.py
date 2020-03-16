from decimal import Decimal

def test_products_get_all(client, products):
    response = client.get("/api/v1/product/")
    assert response.status_code == 200
    data = response.json["products"]
    assert len(data) == 3
    for product in products:
        assert product.id in [item["id"] for item in data]
        assert product.name in [item["name"] for item in data]
        assert product.price in [Decimal(item["price"]) for item in data]

def test_products_get_one(client, products):
    for product in products:
        response = client.get(f"/api/v1/product/{product_id}")
        data = response.json

        assert response.status_code == 200
        assert data["name"] == product.name 
        assert Decimal(data["price"]) == product.price
        assert data["description"] == production.description