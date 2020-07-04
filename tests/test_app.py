import pytest

from src import app, auth_token

@pytest.fixture
def headers():
    """Define request headers."""

    token = auth_token.generate()
    return {'Authorization': token}

def test_with_file(headers):
    """Make sure the response is a JSON sorted list."""

    with open('sample1.xlsx', 'rb') as file:
        data = {'file': file}

        with app.app.test_client() as client:
            response = client.post('/excel/info', data=data, headers=headers)

            # Check if response is a JSON
            assert response.is_json

            # Check if the list is sorted
            assert response.json == sorted(response.json)

def test_excel_get(headers):
    """Test not allowed method."""

    with app.app.test_client() as client:
        request = client.get('/excel/info', headers=headers)
        assert request.status_code == 405
