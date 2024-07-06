import pytest
from fastapi.testclient import TestClient
from fast_zero.app import app


@pytest.fixture
def client():
#client = TestClient(app)  # Arrange (organização do teste)
    return TestClient