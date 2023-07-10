import requests
from configuration import SERVICE_URL


def test_request():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    print(received_posts)
    assert response.status_code == 200
    assert len(received_posts) == 6

