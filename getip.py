import requests


# Function to send a GET request and handle potential errors
def fetch_url(url):
    """
    Sends a GET request to the specified URL and returns the response text.

    :param url: The URL to send the GET request to
    :return: The response text from the URL or an error message
    """
    try:
        # Sending GET request
        response = requests.get(url)
        # If the request was successful, return the content
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        # Handling any request errors (e.g., connection error, timeout, etc.)
        return f"An error occurred: {e}"


# Example usage
url = "http://example.com"
content = fetch_url(url)
print(content)
