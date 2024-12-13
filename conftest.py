import pytest
import requests
import logging
import json
from utils.api_client import APIClient
from utils.json_schema_validator import JSONSchemaValidator
from config import BASE_API_URL, USER_SCHEMA_PATH

# Set up logging configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Construct the full API URL to check if the API is alive
API_URL = f"{BASE_API_URL}/users"  # Replace with any endpoint that checks API health


@pytest.fixture(scope="session", autouse=True)
def check_api_alive():
    """
    This fixture checks that the API is alive before any tests run.
    If the API is not reachable, it will raise an error and stop further tests.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Will raise HTTPError if status is not 200
        logger.info("\nINFO: API is alive and reachable!")  # Log the message
    except requests.RequestException as e:
        pytest.fail(f"\nERROR: API is not reachable. {e}")


@pytest.fixture(scope="session")
def api_client():
    """
    Pytest fixture to initialize the API client.
    """
    client = APIClient(base_url=BASE_API_URL)
    yield client

@pytest.fixture(scope="session")
def schema_validator():
    """
    Pytest fixture to initialize the JSON schema validator.
    """
    yield JSONSchemaValidator
