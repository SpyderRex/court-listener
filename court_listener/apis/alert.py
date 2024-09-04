from ..base import CourtListener

class Alert(CourtListener):
    """
    A client class for interacting with the CourtListener API's alert endpoints.

    The `Alert` class inherits from the `CourtListener` base class and provides methods to 
    interact with the `alerts` and `docket-alerts` endpoints of the CourtListener API.

    It allows users to retrieve data related to alerts and docket alerts, with an option to 
    format the output as prettified JSON.
    """

    def get_alerts(self, **params):
        """
        Retrieve data from the CourtListener API's `alerts` endpoint.

        This method sends a GET request to the `alerts` endpoint, using any provided query 
        parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the alerts. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `alerts` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> alert_client = Alert(api_key="your_api_key")
            >>> response = alert_client.get_alerts(jurisdiction="cal")
            >>> print(response)
        """
        response = self.get_data("alerts", params)
        return self.get_pretty_json(response)

    def get_docket_alerts(self, **params):
        """
        Retrieve data from the CourtListener API's `docket-alerts` endpoint.

        This method sends a GET request to the `docket-alerts` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the docket alerts. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `docket-alerts` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> alert_client = Alert(api_key="your_api_key")
            >>> response = alert_client.get_docket_alerts(jurisdiction="cal")
            >>> print(response)
        """
        response = self.get_data("docket-alerts", params)
        return self.get_pretty_json(response)