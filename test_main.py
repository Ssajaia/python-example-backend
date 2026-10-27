
import pytest

from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/", "welcome to the flask API!"),
        ("/hello", "Hello, World!"),
        ("/status", "OK"),
        ("/health", "Healthy"),
        ("/version", "1.0.0"),
    ],
)
def test_static_endpoints(client, path, expected):
    response = client.get(path)

    assert response.status_code == 200
    assert response.get_data(as_text=True) == expected
    assert response.mimetype == "text/plain"


def test_unknown_endpoint_returns_404(client):
    response = client.get("/unknown")

    assert response.status_code == 404
