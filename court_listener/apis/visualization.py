from ..base import CourtListener

class Visualization(CourtListener):
    """
    A client class for interacting with the CourtListener API's visualization endpoints.

    The `Visualization` class inherits from the `CourtListener` base class and provides methods
    to interact with the visualizations endpoints of the CourtListener API. This class allows users
    to retrieve visualization data in different formats based on the provided query parameters. 
    The JSON responses can be formatted as prettified output based on the class constructor settings.
    """

    def get_visualizations(self, **params):
        """
        Retrieve data from the CourtListener API's `visualizations` endpoint.

        This method sends a GET request to the `visualizations` endpoint using any provided query
        parameters and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the visualization results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `visualizations` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> visualization_client = Visualization(api_key="your_api_key")
            >>> response = visualization_client.get_visualizations(type="bar", date_range="2023-01-01:2023-12-31")
            >>> print(response)
        """
        response = self.get_data("visualizations", params)
        return self.get_pretty_json(response)
        
    def get_visualizations_json(self, **params):
        """
        Retrieve data from the CourtListener API's `visualizations/json` endpoint.

        This method sends a GET request to the `visualizations/json` endpoint using any provided 
        query parameters and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the visualization results in JSON format. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `visualizations/json` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> visualization_client = Visualization(api_key="your_api_key")
            >>> response = visualization_client.get_visualizations_json(type="line", date_range="2023-01-01:2023-12-31")
            >>> print(response)
        """
        response = self.get_data("visualizations/json", params)
        return self.get_pretty_json(response)