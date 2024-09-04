from ..base import CourtListener

class Search(CourtListener):
    """
    A client class for interacting with the CourtListener API's search endpoint.

    The `Search` class inherits from the `CourtListener` base class and provides methods 
    to interact with the search endpoint of the CourtListener API. This class allows users 
    to retrieve search results based on various query parameters. The JSON response can 
    be formatted as prettified output based on the class constructor settings.
    """

    def get_search(self, **params):
        """
        Retrieve data from the CourtListener API's `search` endpoint.

        This method sends a GET request to the `search` endpoint, using any provided query 
        parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the search results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `search` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> search_client = Search(api_key="your_api_key")
            >>> response = search_client.get_search(query="case law", start_date="2023-01-01", end_date="2023-12-31")
            >>> print(response)
        """
        response = self.get_data("search", params)
        return self.get_pretty_json(response)