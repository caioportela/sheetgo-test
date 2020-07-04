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

def test_without_file(headers):
    """See what happens when there's no xlsx file."""

    with app.app.test_client() as client:
        response = client.post('/excel/info', headers=headers)
        assert response.status_code == 400
        assert response.get_data(as_text=True) == '400 Bad Request - No file sent\n'

def test_excel_get(headers):
    """Test not allowed method."""

    with app.app.test_client() as client:
        response = client.get('/excel/info', headers=headers)
        assert response.status_code == 405

def test_convert_jpeg(headers):
    """Make sure output is a png image."""

    with open('image1.jpeg', 'rb') as file:
        data = {'file': file, 'format': 'png'}

        with app.app.test_client() as client:
            response = client.post('/image/convert', data=data, headers=headers)

            # Check if jpeg has been converted to png
            assert response.mimetype == 'image/png'

def test_convert_png(headers):
    """Make sure output is a jpeg image."""

    with open('image2.png', 'rb') as file:
        data = {'file': file, 'format': 'jpeg'}

        with app.app.test_client() as client:
            response = client.post('/image/convert', data=data, headers=headers)

            # Check if png has been converted to jpeg
            assert response.mimetype == 'image/jpeg'

def test_without_image(headers):
    """Check response when there's no image."""

    with app.app.test_client() as client:
        response = client.post('/image/convert', headers=headers)
        assert response.status_code == 400
        assert response.get_data(as_text=True) == '400 Bad Request - No format sent\n'

def test_image_get(headers):
    """Test not allowed method."""

    with app.app.test_client() as client:
        response = client.get('/image/convert', headers=headers)
        assert response.status_code == 405

def test_dropbox_token(headers):
    """Check response when the dropbox access token is not passed."""

    with app.app.test_client() as client:
        response = client.post('image/convert/fromdropbox', headers=headers)
        assert response.status_code == 403
        assert response.get_data(as_text=True) == '403 Forbidden - No dropbox access token sent\n'
