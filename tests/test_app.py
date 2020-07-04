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
            request = client.post('/excel/info', data=data, headers=headers)

            # Check if response is a JSON
            assert request.is_json

            # Check if the list is sorted
            assert request.json == sorted(request.json)
