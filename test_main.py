from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_decode_default_url():
    response = client.post('/decode', json={'url': 'http://short.est/MQ'})
    assert response.status_code == 200
    assert response.json() == {
        'original_url': 'https://www.example_url.com/',
        'shortened_url': 'http://short.est/MQ',
    }

def test_decode_not_existing_url():
    response = client.post('/decode', json={'url': 'http://short.est/Mg'})
    assert response.status_code == 404
    assert response.json() == {
        'detail' : 'URL not found'
    }

def test_encode_default_url():
    response = client.post('/encode', json={'url': 'https://www.example_url.com/'})
    assert response.status_code == 302
    assert response.json() == {
        'original_url': 'https://www.example_url.com/',
        'shortened_url': 'http://short.est/MQ',
    }

def test_encode_create_url():
    response = client.post('/encode', json={'url': 'https://www.example2_url.com/'})
    assert response.status_code == 201
    assert response.json() == {
        'original_url': 'https://www.example2_url.com/',
        'shortened_url': 'http://short.est/Mg',
    }

def test_encode_check_created_url():
    response = client.post('/encode', json={'url': 'https://www.example2_url.com/'})
    assert response.status_code == 302
    assert response.json() == {
        'original_url': 'https://www.example2_url.com/',
        'shortened_url': 'http://short.est/Mg',
    }

def test_decode_retrieve_created_url():
    response = client.post('/decode', json={'url': 'http://short.est/Mg'})
    assert response.status_code == 200
    assert response.json() == {
        'original_url': 'https://www.example2_url.com/',
        'shortened_url': 'http://short.est/Mg',
    }

def test_decode_incorrect_urls():
    response = client.post('/decode', json={'url': 'http://short.est/gM'})
    assert response.status_code == 400
    assert response.json() == {
        'detail' : 'URL invalid'
    }
    response = client.post('/decode', json={'url': 'http://short.est/Mgh'})
    assert response.status_code == 400
    assert response.json() == {
        'detail' : 'URL invalid'
    }