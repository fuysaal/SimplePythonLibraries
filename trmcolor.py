from termcolor import colored


# Function to print text in a specified color
def print_colored(text, color):
    """
    Prints the text in the specified color.

    :param text: The text to be printed
    :param color: The color of the text (e.g., 'red', 'blue', 'green', etc.)
    """
    print(colored(text, color))


# Example usage
print_colored("Red Team", "red")
print_colored("Blue Team", "blue")
