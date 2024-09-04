from ..base import CourtListener

class RECAP(CourtListener):
    """
    A client class for interacting with the CourtListener API's RECAP-related endpoints.

    The `RECAP` class inherits from the `CourtListener` base class and provides methods 
    to interact with various RECAP data endpoints. This class allows users to retrieve 
    data from endpoints related to RECAP fetch, RECAP data, and RECAP email. The JSON 
    response can be formatted as prettified output based on the class constructor settings.
    """

    def get_recap_fetch(self, **params):
        """
        Retrieve data from the CourtListener API's `recap-fetch` endpoint.

        This method sends a GET request to the `recap-fetch` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the recap fetch results. These parameters will be appended to the 
                      API request.

        Returns:
            str: A JSON string representing the response from the `recap-fetch` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> recap_client = RECAP(api_key="your_api_key")
            >>> response = recap_client.get_recap_fetch(fetch_id="abc123")
            >>> print(response)
        """
        response = self.get_data("recap-fetch", params)
        return self.get_pretty_json(response)
        
    def get_recap(self, **params):
        """
        Retrieve data from the CourtListener API's `recap` endpoint.

        This method sends a GET request to the `recap` endpoint, using any provided query 
        parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the recap results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `recap` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> recap_client = RECAP(api_key="your_api_key")
            >>> response = recap_client.get_recap(query="case_summary")
            >>> print(response)
        """
        response = self.get_data("recap", params)
        return self.get_pretty_json(response)
        
    def get_recap_email(self, **params):
        """
        Retrieve data from the CourtListener API's `recap-email` endpoint.

        This method sends a GET request to the `recap-email` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the recap email results. These parameters will be appended to the 
                      API request.

        Returns:
            str: A JSON string representing the response from the `recap-email` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> recap_client = RECAP(api_key="your_api_key")
            >>> response = recap_client.get_recap_email(email_id="xyz789")
            >>> print(response)
        """
        response = self.get_data("recap-email", params)
        return self.get_pretty_json(response)