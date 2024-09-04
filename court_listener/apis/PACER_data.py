from ..base import CourtListener

class PACERData(CourtListener):
    """
    A client class for interacting with the CourtListener API's PACER-related endpoints.

    The `PACERData` class inherits from the `CourtListener` base class and provides methods 
    to interact with various PACER data endpoints. This class allows users to retrieve 
    data from multiple endpoints related to docket entries, recap documents, parties, 
    attorneys, and more. The JSON response can be formatted as prettified output based 
    on the class constructor settings.
    """

    def get_docket_entries(self, **params):
        """
        Retrieve data from the CourtListener API's `docket-entries` endpoint.

        This method sends a GET request to the `docket-entries` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the docket entries results. These parameters will be appended to the 
                      API request.

        Returns:
            str: A JSON string representing the response from the `docket-entries` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> pacer_data_client = PACERData(api_key="your_api_key")
            >>> response = pacer_data_client.get_docket_entries(case_number="12345")
            >>> print(response)
        """
        response = self.get_data("docket-entries", params)
        return self.get_pretty_json(response)
        
    def get_recap_documents(self, **params):
        """
        Retrieve data from the CourtListener API's `recap-documents` endpoint.

        This method sends a GET request to the `recap-documents` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the recap documents results. These parameters will be appended to the 
                      API request.

        Returns:
            str: A JSON string representing the response from the `recap-documents` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> pacer_data_client = PACERData(api_key="your_api_key")
            >>> response = pacer_data_client.get_recap_documents(document_id="67890")
            >>> print(response)
        """
        response = self.get_data("recap-documents", params)
        return self.get_pretty_json(response)
        
    def get_parties(self, **params):
        """
        Retrieve data from the CourtListener API's `parties` endpoint.

        This method sends a GET request to the `parties` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the parties results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `parties` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> pacer_data_client = PACERData(api_key="your_api_key")
            >>> response = pacer_data_client.get_parties(case_id="abc123")
            >>> print(response)
        """
        response = self.get_data("parties", params)
        return self.get_pretty_json(response)
        
    def get_attorneys(self, **params):
        """
        Retrieve data from the CourtListener API's `attorneys` endpoint.

        This method sends a GET request to the `attorneys` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the attorneys results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `attorneys` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> pacer_data_client = PACERData(api_key="your_api_key")
            >>> response = pacer_data_client.get_attorneys(lawyer_id="xyz789")
            >>> print(response)
        """
        response = self.get_data("attorneys", params)
        return self.get_pretty_json(response)
        
    def get_originating_court_information(self, **params):
        """
        Retrieve data from the CourtListener API's `originating-court-information` endpoint.

        This method sends a GET request to the `originating-court-information` endpoint, 
        using any provided query parameters, and returns the JSON response, which can be 
        optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the originating court information results. These parameters will be 
                      appended to the API request.

        Returns:
            str: A JSON string representing the response from the `originating-court-information` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> pacer_data_client = PACERData(api_key="your_api_key")
            >>> response = pacer_data_client.get_originating_court_information(court_id="123")
            >>> print(response)
        """
        response = self.get_data("originating-court-information", params)
        return self.get_pretty_json(response)
        
    def get_fjc_integrated_database(self, **params):
        """
        Retrieve data from the CourtListener API's `fjc-integrated-database` endpoint.

        This method sends a GET request to the `fjc-integrated-database` endpoint, using any 
        provided query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the FJC integrated database results. These parameters will be appended 
                      to the API request.

        Returns:
            str: A JSON string representing the response from the `fjc-integrated-database` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> pacer_data_client = PACERData(api_key="your_api_key")
            >>> response = pacer_data_client.get_fjc_integrated_database(database_id="456")
            >>> print(response)
        """
        response = self.get_data("fjc-integrated-database", params)
        return self.get_pretty_json(response)
        
    def get_recap_query(self, **params):
        """
        Retrieve data from the CourtListener API's `recap-query` endpoint.

        This method sends a GET request to the `recap-query` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the recap query results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `recap-query` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> pacer_data_client = PACERData(api_key="your_api_key")
            >>> response = pacer_data_client.get_recap_query(query="some_query")
            >>> print(response)
        """
        response = self.get_data("recap-query", params)
        return self.get_pretty_json(response)