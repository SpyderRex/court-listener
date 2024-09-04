# court_listener

`court_listener` is a Python client library for interacting with the Court Listener API. It provides an easy way to access and query court data from the Court Listener API, which offers access to a wealth of legal information including case law, opinions, and more.

## Features

- **Simple API Interaction**: Easily interact with the Court Listener API using a straightforward Python client.
- **Prettified JSON Output**: By default JSON responses are prettified for better readability. This can be changed by setting prettify to False in the class constructor.
- **Error Handling**: Includes built-in error handling to manage API request issues gracefully.

## Installation

You can install `court_listener` via pip:

```bash
pip install court-listener
```

## Usage

### Making API Requests

You can interact with different API endpoints using specialized classes provided within the `apis` module. For example, to use the search functionality:

```python
from court_listener.apis.search import Search

search_client = Search(api_key="your_api_key")
response = search_client.get_search(query="case law", start_date="2023-01-01", end_date="2023-12-31")
print(response)
```

## Error Handling

The library includes error handling to manage potential issues with API requests. Ensure that any API errors are handled appropriately in your implementation.

## Court Listener Documentation

Users should reference the Court Listener docs for more information. According to the docs, "Our APIs allow 5,000 queries per hour to authenticated users. Unauthenticated users are allowed 100 queries per day for experimentation." To read further and get your own api key, visit their site [here](https://www.courtlistener.com/help/api/rest/)

## Contributing

Contributions are welcome! Please submit issues or pull requests on [GitHub](https://github.com/SpyderRex/court_listener).

## License

`court_listener` is open-source software licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [billyjohnsonauthor@gmail.com](mailto:billyjohnsonauthor@gmail.com).
