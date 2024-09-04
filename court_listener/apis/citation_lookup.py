from ..base import CourtListener

class CitationLookup(CourtListener):
    """
    A client class for interacting with the CourtListener API's citation lookup endpoint.

    The `CitationLookup` class inherits from the `CourtListener` base class and provides 
    a method to interact with the `citation-lookup` endpoint. This class allows users 
    to retrieve citation lookup data, with an option to format the output as prettified JSON.
    """

    def get_citation_lookup(self, **params):
        """
        Retrieve data from the CourtListener API's `citation-lookup` endpoint.

        This method sends a GET request to the `citation-lookup` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the citation lookup results. These parameters will be appended to the 
                      API request.

        Returns:
            str: A JSON string representing the response from the `citation-lookup` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> citation_client = CitationLookup(api_key="your_api_key")
            >>> response = citation_client.get_citation_lookup(citation="2024-ABC-123")
            >>> print(response)
        """
        response = self.get_data("citation-lookup", params)
        return self.get_pretty_json(response)