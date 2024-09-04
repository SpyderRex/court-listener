from ..base import CourtListener

class FinancialDisclosure(CourtListener):
    """
    A client class for interacting with the CourtListener API's financial disclosure endpoints.

    The `FinancialDisclosure` class inherits from the `CourtListener` base class and provides 
    methods to interact with various financial disclosure-related endpoints. These endpoints 
    include financial disclosures, investments, disclosure positions, agreements, non-investment 
    incomes, spouse incomes, reimbursements, gifts, and debts. The class allows users to retrieve 
    data from these endpoints and format the output as prettified JSON if desired.
    """

    def get_financial_disclosures(self, **params):
        """
        Retrieve data from the CourtListener API's `financial-disclosures` endpoint.

        This method sends a GET request to the `financial-disclosures` endpoint, using any provided 
        query parameters, and returns the JSON response, which can be optionally prettified.

        Args:
            **params: Arbitrary keyword arguments representing query parameters to filter 
                      the financial disclosures results. These parameters will be appended 
                      to the API request.

        Returns:
            str: A JSON string representing the response from the `financial-disclosures` endpoint, 
                 prettified if the `prettify` parameter in the class constructor is set to True.

        Example:
            >>> financial_disclosure_client = FinancialDisclosure(api_key="your_api_key")
            >>> response = financial_disclosure_client.get_financial_disclosures(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("financial-disclosures", params)
        return self.get_pretty_json(response)
    
    def get_investments(self, **params):
        """
        Retrieve data from the CourtListener API's `investments` endpoint.

        Args:
            **params: Query parameters to filter the investments results.

        Returns:
            str: A JSON string representing the response from the `investments` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_investments(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("investments", params)
        return self.get_pretty_json(response)
    
    def get_disclosure_positions(self, **params):
        """
        Retrieve data from the CourtListener API's `disclosure-positions` endpoint.

        Args:
            **params: Query parameters to filter the disclosure positions results.

        Returns:
            str: A JSON string representing the response from the `disclosure-positions` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_disclosure_positions(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("disclosure-positions", params)
        return self.get_pretty_json(response)
    
    def get_agreements(self, **params):
        """
        Retrieve data from the CourtListener API's `agreements` endpoint.

        Args:
            **params: Query parameters to filter the agreements results.

        Returns:
            str: A JSON string representing the response from the `agreements` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_agreements(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("agreements", params)
        return self.get_pretty_json(response)
    
    def get_non_investment_incomes(self, **params):
        """
        Retrieve data from the CourtListener API's `non-investment-incomes` endpoint.

        Args:
            **params: Query parameters to filter the non-investment incomes results.

        Returns:
            str: A JSON string representing the response from the `non-investment-incomes` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_non_investment_incomes(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("non-investment-incomes", params)
        return self.get_pretty_json(response)
    
    def get_spouse_incomes(self, **params):
        """
        Retrieve data from the CourtListener API's `spouse-incomes` endpoint.

        Args:
            **params: Query parameters to filter the spouse incomes results.

        Returns:
            str: A JSON string representing the response from the `spouse-incomes` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_spouse_incomes(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("spouse-incomes", params)
        return self.get_pretty_json(response)
    
    def get_reimbursements(self, **params):
        """
        Retrieve data from the CourtListener API's `reimbursements` endpoint.

        Args:
            **params: Query parameters to filter the reimbursements results.

        Returns:
            str: A JSON string representing the response from the `reimbursements` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_reimbursements(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("reimbursements", params)
        return self.get_pretty_json(response)
    
    def get_gifts(self, **params):
        """
        Retrieve data from the CourtListener API's `gifts` endpoint.

        Args:
            **params: Query parameters to filter the gifts results.

        Returns:
            str: A JSON string representing the response from the `gifts` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_gifts(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("gifts", params)
        return self.get_pretty_json(response)
    
    def get_debts(self, **params):
        """
        Retrieve data from the CourtListener API's `debts` endpoint.

        Args:
            **params: Query parameters to filter the debts results.

        Returns:
            str: A JSON string representing the response from the `debts` endpoint, 
                 optionally prettified.

        Example:
            >>> response = financial_disclosure_client.get_debts(judge_id="123")
            >>> print(response)
        """
        response = self.get_data("debts", params)
        return self.get_pretty_json(response)