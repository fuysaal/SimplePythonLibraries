import requests


def is_valid_url(url):
    """ Check if the given URL is valid. """
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Error: The URL must start with 'http://' or 'https://'.")
        return False
    return True


def monitor_status(target):
    """ Monitor the status code of the target URL. """
    try:
        while True:
            # Send a GET request
            r = requests.get(target)
            print(f"Status Code: {r.status_code}")

            # Ask if the user wants to continue or exit
            user_input = input("Press Enter to continue, or type 'exit' to stop: ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break
    except requests.exceptions.RequestException as e:
        # Handle any request errors (e.g., connection issues, timeouts)
        print(f"An error occurred: {e}")


def main():
    # Get URL input from the user
    target = input("Enter the target URL: ").strip()

    if is_valid_url(target):
        monitor_status(target)


# Run the program
if __name__ == "__main__":
    main()
