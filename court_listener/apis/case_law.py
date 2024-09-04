import requests

from ..base import CourtListener
from ..error_handling import handle_api_errors

class CaseLaw(CourtListener):
    """
    A client class for interacting with the CourtListener API's case law-related endpoints.

    The `CaseLaw` class inherits from the `CourtListener` base class and provides methods 
    to interact with various endpoints related to case law, including `dockets`, `clusters`, 
    `opinions`, `courts`, `docket-tags`, and `tags`.

    It allows users to retrieve case law data from these endpoints, with an option to 
    format the output as prettified JSON.
    """

    def get_dockets(self, **params):
        """
        Retrieve data from the CourtListener API's `dockets` endpoint.

        This method sends a GET request to the `dockets` endpoint, using any provided query 
        parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the dockets. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `dockets` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> caselaw_client = CaseLaw(api_key="your_api_key")
            >>> response = caselaw_client.get_dockets(jurisdiction="cal")
            >>> print(response)
        """
        response = self.get_data("dockets", params)
        return self.get_pretty_json(response)

    def get_clusters(self, **params):
        """
        Retrieve data from the CourtListener API's `clusters` endpoint.

        This method sends a GET request to the `clusters` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the clusters. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `clusters` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> caselaw_client = CaseLaw(api_key="your_api_key")
            >>> response = caselaw_client.get_clusters(jurisdiction="cal")
            >>> print(response)
        """
        response = self.get_data("clusters", params)
        return self.get_pretty_json(response)

    def get_opinions(self, **params):
        """
        Retrieve data from the CourtListener API's `opinions` endpoint.

        This method sends a GET request to the `opinions` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the opinions. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `opinions` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> caselaw_client = CaseLaw(api_key="your_api_key")
            >>> response = caselaw_client.get_opinions(citation="2024-ABC-123")
            >>> print(response)
        """
        response = self.get_data("opinions", params)
        return self.get_pretty_json(response)

    def get_courts(self, **params):
        """
        Retrieve data from the CourtListener API's `courts` endpoint.

        This method sends a GET request to the `courts` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the courts. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `courts` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> caselaw_client = CaseLaw(api_key="your_api_key")
            >>> response = caselaw_client.get_courts(jurisdiction="cal")
            >>> print(response)
        """
        response = self.get_data("courts", params)
        return self.get_pretty_json(response)

    def get_docket_tags(self, **params):
        """
        Retrieve data from the CourtListener API's `docket-tags` endpoint.

        This method sends a GET request to the `docket-tags` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the docket tags. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `docket-tags` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> caselaw_client = CaseLaw(api_key="your_api_key")
            >>> response = caselaw_client.get_docket_tags(jurisdiction="cal")
            >>> print(response)
        """
        response = self.get_data("docket-tags", params)
        return self.get_pretty_json(response)

    def get_tags(self, **params):
        """
        Retrieve data from the CourtListener API's `tags` endpoint.

        This method sends a GET request to the `tags` endpoint, using any provided query 
        parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the tags. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `tags` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> caselaw_client = CaseLaw(api_key="your_api_key")
            >>> response = caselaw_client.get_tags(tag="environmental-law")
            >>> print(response)
        """
        response = self.get_data("tags", params)
        return self.get_pretty_json(response)