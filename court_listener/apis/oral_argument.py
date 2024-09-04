from ..base import CourtListener

class OralArgument(CourtListener):
    """
    A client class for interacting with the CourtListener API's oral argument-related endpoints.

    The `OralArgument` class inherits from the `CourtListener` base class and provides methods 
    to interact with the `audio` endpoint. This class allows users to retrieve data related to 
    oral argument audio recordings and format the output as prettified JSON if desired.
    """

    def get_audio(self, **params):
        """
        Retrieve data from the CourtListener API's `audio` endpoint.

        This method sends a GET request to the `audio` endpoint, using any provided query 
        parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the audio results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `audio` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> oral_argument_client = OralArgument(api_key="your_api_key")
            >>> response = oral_argument_client.get_audio(court="ca9")
            >>> print(response)
        """
        response = self.get_data("audio", params)
        return self.get_pretty_json(response)