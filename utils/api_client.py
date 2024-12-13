import requests


class APIClient:
    def __init__(self, base_url, auth=None):
        """
        Initialize the API client.

        :param base_url: Base URL for the API.
        :param auth: Optional authentication (e.g., token or tuple for Basic Auth).
        """
        self.base_url = base_url
        self.auth = auth

    def _get_headers(self):
        headers = {"Content-Type": "application/json"}
        if isinstance(self.auth, str):  # Token-based auth
            headers["Authorization"] = f"Bearer {self.auth}"
        return headers

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}/{endpoint}", headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self._get_headers())
        response.raise_for_status()
        return response.status_code
