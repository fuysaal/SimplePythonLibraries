from pynput.keyboard import Listener

# Function to handle key press events
def on_press(key):
    try:
        # Print the key pressed
        print(f"Key {key} pressed")
    except Exception as e:
        # Handle errors (for example, non-character keys might raise an error)
        print(f"Error occurred: {e}")

# Starting the listener to listen to key presses
def start_listener():
    # Creating and starting the listener
    with Listener(on_press=on_press) as listener:
        listener.join()

# Example usage
start_listener()
