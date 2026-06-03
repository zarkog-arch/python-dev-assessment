import requests
import json
from requests.exceptions import RequestException


def fetch_and_display_users(num_users):

    API_URL = "https://jsonplaceholder.typicode.com/users"

    # 1. Error Handling for Network Issues and Non-200 HTTP Status Codes
    try:
        response = requests.get(API_URL, timeout=10)

        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

    except RequestException as e:
        print(f"Error: Network issue or non-200 HTTP status code occurred: {e}")
        return None

    # 2. Error Handling for JSON Decoding and Structure
    try:
        users_data = response.json()

        if not isinstance(users_data, list):
            print(
                "Error: API response was successfully retrieved but is not a list of users."
            )
            return None

        users_to_process = users_data[:num_users]

        print(
            f"--- Displaying details for {len(users_to_process)} out of {len(users_data)} total users ---"
        )

        for user in users_to_process:
            # Error Handling for missing keys (unexpected JSON structure)
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]  # Nested key extraction

                print(f"Name: {name}, Email: {email}, City: {city}")

            except KeyError as e:
                print(
                    f"Error: Missing expected key in a user object: {e}. Skipping this user."
                )
            except TypeError as e:
                print(
                    f"Error: Unexpected data type encountered while parsing user data: {e}. Skipping this user."
                )

    except json.JSONDecodeError:
        print("Error: Failed to decode JSON response (API returned non-JSON data).")
        return None
    except Exception as e:
        # Catch any other unexpected processing errors
        print(f"An unexpected error occurred during data processing: {e}")
        return None


if __name__ == "__main__":
    # Example calls from file with tasks:

    print("\n--- Example 1: fetch_and_display_users(4) ---")
    fetch_and_display_users(4)

    print(
        "\n--- Example 2: fetch_and_display_users(16) (API only returns 10 users) ---"
    )
    fetch_and_display_users(16)
