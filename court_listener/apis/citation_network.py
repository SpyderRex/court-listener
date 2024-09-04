from ..base import CourtListener

class CitationNetwork(CourtListener):
    """
    A client class for interacting with the CourtListener API's citation network endpoints.

    The `CitationNetwork` class inherits from the `CourtListener` base class and provides 
    a method to interact with the `opinions-cited` endpoint. This class allows users to 
    retrieve data related to opinions cited in the citation network, with an option to 
    format the output as prettified JSON.
    """

    def get_opinions_cited(self, **params):
        """
        Retrieve data from the CourtListener API's `opinions-cited` endpoint.

        This method sends a GET request to the `opinions-cited` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the opinions cited results. These parameters will be appended to the 
                      API request.

        Returns:
            str: A JSON string representing the response from the `opinions-cited` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> citation_network_client = CitationNetwork(api_key="your_api_key")
            >>> response = citation_network_client.get_opinions_cited(case_id="123456")
            >>> print(response)
        """
        response = self.get_data("opinions-cited", params)
        return self.get_pretty_json(response)