import requests

# Define error messages for specific HTTP status codes
HTTP_STATUS_MESSAGES = {
    400: "Bad Request: The server could not understand the request.",
    401: "Unauthorized: Authentication is required or has failed.",
    403: "Forbidden: The server understands the request but refuses to authorize it.",
    404: "Not Found: The requested resource could not be found.",
    405: "Method Not Allowed: The method specified in the request is not allowed for the resource.",
    408: "Request Timeout: The server timed out waiting for the request.",
    500: "Internal Server Error: The server encountered an unexpected condition.",
    502: "Bad Gateway: The server received an invalid response from an upstream server.",
    503: "Service Unavailable: The server is currently unable to handle the request.",
    504: "Gateway Timeout: The server, while acting as a gateway, timed out waiting for an upstream server."
}

def handle_api_errors(func):
    """
    A decorator to handle API errors in HTTP requests.

    This decorator wraps around a function that makes HTTP requests using the `requests` library. 
    It handles various exceptions that can occur during the request process and returns a detailed 
    error message when an exception is raised.

    The decorator catches specific exceptions like `HTTPError`, `ConnectionError`, `Timeout`, and 
    `RequestException`, as well as any other general exceptions, returning a dictionary with error 
    details instead of allowing the exception to propagate.

    Args:
        func (function): The function to be decorated, typically one that makes an HTTP request.

    Returns:
        function: A wrapped function that executes the original function and handles exceptions, 
                  returning a dictionary with error details if an exception occurs.

    Example:
        >>> @handle_api_errors
        >>> def get_data_from_api():
        >>>     response = requests.get('https://api.example.com/data')
        >>>     return response
        >>> 
        >>> response = get_data_from_api()
        >>> if 'error' in response:
        >>>     print(response['message'])
        >>> else:
        >>>     print(response.json())
    """
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            # Raise HTTPError if the response indicates an error
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            status_code = http_err.response.status_code
            message = HTTP_STATUS_MESSAGES.get(status_code, "An HTTP error occurred.")
            return {
                "error": "HTTP error occurred",
                "message": message,
                "status_code": status_code,
                "details": str(http_err)
            }
        except requests.exceptions.ConnectionError as conn_err:
            return {
                "error": "Connection error occurred",
                "message": str(conn_err)
            }
        except requests.exceptions.Timeout as timeout_err:
            return {
                "error": "Timeout error occurred",
                "message": str(timeout_err)
            }
        except requests.exceptions.RequestException as req_err:
            return {
                "error": "Request exception occurred",
                "message": str(req_err)
            }
        except Exception as general_err:
            return {
                "error": "An unexpected error occurred",
                "message": str(general_err)
            }
    return wrapper