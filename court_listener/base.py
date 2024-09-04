import json
import requests
from court_listener.error_handling import handle_api_errors

class CourtListener:
    """
    A client for interacting with the Court Listener API.

    This class allows users to make authenticated requests to the Court Listener API 
    and retrieve JSON data, which can be optionally prettified.

    Attributes:
        api_key (str): The API key for authenticating requests.
        prettify (bool): Flag indicating whether to prettify the JSON output (default is True).
        headers (dict): HTTP headers for the API requests, including Authorization and Accept.
        base_url (str): The base URL for the Court Listener API (default is "https://www.courtlistener.com/api/rest/v3").
    """

    def __init__(self, api_key, base_url="https://www.courtlistener.com/api/rest/v3", prettify=True):
        """
        Initializes the CourtListener client.

        Args:
            api_key (str): The API key used for authenticating requests to the Court Listener API.
            base_url (str, optional): The base URL for the Court Listener API. Defaults to "https://www.courtlistener.com/api/rest/v3".
            prettify (bool, optional): Whether to prettify the JSON output. Defaults to True.
        """
        self.api_key = api_key
        self.prettify = prettify
        self.headers = {
            "Authorization": f"Token {self.api_key}",
            "Accept": "application/json; indent=2" if self.prettify else "application/json"
        }
        self.base_url = base_url

    @handle_api_errors
    def get_data(self, endpoint, params=None):
        """
        Sends a GET request to the specified API endpoint.

        Args:
            endpoint (str): The specific API endpoint to be appended to the base URL.
            params (dict, optional): A dictionary of query parameters to include in the request. Defaults to None.

        Returns:
            requests.Response: The response object returned by the API.

        Raises:
            HTTPError: If the API request fails, an HTTPError will be raised by the error handling decorator.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def get_pretty_json(self, response):
        """
        Converts the API response to JSON format, optionally prettifying the output.

        Args:
            response (requests.Response or dict): The response object returned by the API or a dictionary in case of error.

        Returns:
            str: A JSON-formatted string, prettified if the `prettify` attribute is True.

        Example:
            >>> response = court_listener.get_data('opinions/')
            >>> print(court_listener.get_pretty_json(response))
        """
        if isinstance(response, requests.Response):
            json_data = response.json()
        else:
            json_data = response

        if self.prettify:
            pretty_json = json.dumps(json_data, indent=2)
        else:
            pretty_json = json.dumps(json_data)

        return pretty_json