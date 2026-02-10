
import requests
import json

def get_example(url="https://jsonplaceholder.typicode.com/todos/1"):
    """
    Demonstrates a simple GET request using the requests library.
    Fetches data from the specified URL.
    """
    print(f"Making GET request to: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()
        print("GET Request Successful!")
        print("Status Code:", response.status_code)
        print("Response Body:")
        print(json.dumps(data, indent=2))
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    return None

def post_example(url="https://jsonplaceholder.typicode.com/posts"):
    """
    Demonstrates a simple POST request using the requests library.
    Sends JSON data to the specified URL.
    """
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}

    print(f"
Making POST request to: {url}")
    print("Payload:", json.dumps(payload, indent=2))
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()
        print("POST Request Successful!")
        print("Status Code:", response.status_code)
        print("Response Body:")
        print(json.dumps(data, indent=2))
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    return None

if __name__ == "__main__":
    print("This script demonstrates how to make API requests using Python's 'requests' library.")
    print("Before running, ensure you have the 'requests' library installed:")
    print("  pip install requests")
    print("-" * 50)

    # Example GET Request
    get_example()

    print("-" * 50)

    # Example POST Request
    post_example()
