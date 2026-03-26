import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200

def test_recipes_api(client):
    """Test the recipes API endpoint returns data."""
    response = client.get('/api/recipes')
    assert response.status_code == 200
    assert response.is_json
