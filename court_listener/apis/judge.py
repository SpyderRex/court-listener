from ..base import CourtListener

class Judge(CourtListener):
    """
    A client class for interacting with the CourtListener API's judge-related endpoints.

    The `Judge` class inherits from the `CourtListener` base class and provides methods 
    to interact with various endpoints related to judges and their background information. 
    These endpoints include people, positions, political affiliations, educations, ABA 
    ratings, retention events, sources, disclosure typeahead, and schools. The class 
    allows users to retrieve data from these endpoints and format the output as prettified 
    JSON if desired.
    """

    def get_people(self, **params):
        """
        Retrieve data from the CourtListener API's `people` endpoint.

        This method sends a GET request to the `people` endpoint, using any provided query 
        parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the people results. These parameters will be appended to the API request.

        Returns:
            str: A JSON string representing the response from the `people` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> judge_client = Judge(api_key="your_api_key")
            >>> response = judge_client.get_people(last_name="Smith")
            >>> print(response)
        """
        response = self.get_data("people", params)
        return self.get_pretty_json(response)
    
    def get_positions(self, **params):
        """
        Retrieve data from the CourtListener API's `positions` endpoint.

        Args:
            **params: Query parameters to filter the positions results.

        Returns:
            str: A JSON string representing the response from the `positions` endpoint, 
                 optionally prettified.

        Example:
            >>> response = judge_client.get_positions(court="Supreme Court")
            >>> print(response)
        """
        response = self.get_data("positions", params)
        return self.get_pretty_json(response)
    
    def get_political_affiliations(self, **params):
        """
        Retrieve data from the CourtListener API's `political-affiliations` endpoint.

        Args:
            **params: Query parameters to filter the political affiliations results.

        Returns:
            str: A JSON string representing the response from the `political-affiliations` 
                 endpoint, optionally prettified.

        Example:
            >>> response = judge_client.get_political_affiliations(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("political-affiliations", params)
        return self.get_pretty_json(response)
    
    def get_educations(self, **params):
        """
        Retrieve data from the CourtListener API's `educations` endpoint.

        Args:
            **params: Query parameters to filter the educations results.

        Returns:
            str: A JSON string representing the response from the `educations` endpoint, 
                 optionally prettified.

        Example:
            >>> response = judge_client.get_educations(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("educations", params)
        return self.get_pretty_json(response)
    
    def get_aba_ratings(self, **params):
        """
        Retrieve data from the CourtListener API's `aba-ratings` endpoint.

        Args:
            **params: Query parameters to filter the ABA ratings results.

        Returns:
            str: A JSON string representing the response from the `aba-ratings` endpoint, 
                 optionally prettified.

        Example:
            >>> response = judge_client.get_aba_ratings(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("aba-ratings", params)
        return self.get_pretty_json(response)
    
    def get_retention_events(self, **params):
        """
        Retrieve data from the CourtListener API's `retention-events` endpoint.

        Args:
            **params: Query parameters to filter the retention events results.

        Returns:
            str: A JSON string representing the response from the `retention-events` endpoint, 
                 optionally prettified.

        Example:
            >>> response = judge_client.get_retention_events(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("retention-events", params)
        return self.get_pretty_json(response)
    
    def get_sources(self, **params):
        """
        Retrieve data from the CourtListener API's `sources` endpoint.

        Args:
            **params: Query parameters to filter the sources results.

        Returns:
            str: A JSON string representing the response from the `sources` endpoint, 
                 optionally prettified.

        Example:
            >>> response = judge_client.get_sources(source_type="Biographical")
            >>> print(response)
        """
        response = self.get_data("sources", params)
        return self.get_pretty_json(response)
    
    def get_disclosure_typeahead(self, **params):
        """
        Retrieve data from the CourtListener API's `disclosure-typeahead` endpoint.

        Args:
            **params: Query parameters to filter the disclosure typeahead results.

        Returns:
            str: A JSON string representing the response from the `disclosure-typeahead` 
                 endpoint, optionally prettified.

        Example:
            >>> response = judge_client.get_disclosure_typeahead(query="John")
            >>> print(response)
        """
        response = self.get_data("disclosure-typeahead", params)
        return self.get_pretty_json(response)

    def get_schools(self, **params):
        """
        Retrieve data from the CourtListener API's `schools` endpoint.

        Args:
            **params: Query parameters to filter the schools results.

        Returns:
            str: A JSON string representing the response from the `schools` endpoint, 
                 optionally prettified.

        Example:
            >>> response = judge_client.get_schools(name="Harvard")
            >>> print(response)
        """
        response = self.get_data("schools", params)
        return self.get_pretty_json(response)