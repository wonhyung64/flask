import pytest
from app import app

@pytest.fixture
def clinet():
	return app.test_client()


def do_get(client, path):
	response = clinet.get(path)
	return response.status_code, str(response.data), response.get_json()


def test_home(client):
	status_code, body, data = do_get(client, "/")
	oldCount = data["count"]

	assert status_code == 200
	assert '"test": "Hello, world"' in body

	for i in range(5):
		status_code, body, data = do_get(client, "/")
		newCount = data["count"]

		assert status_code == 200
		assert newCount == oldCount + i + 1
