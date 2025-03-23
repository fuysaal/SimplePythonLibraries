# Function to read the content of a file
def read_file(file_name):
    """
    Reads the content of a file and returns the content.

    :param file_name: The name or path of the file to read
    :return: The content of the file or an error message
    """
    try:
        # Open the file in read mode
        with open(file_name, "r") as f:
            # Return the content of the file
            return f.read()
    except FileNotFoundError:
        # Handle case when the file doesn't exist
        return f"Error: The file '{file_name}' was not found."
    except IOError as e:
        # Handle other I/O errors
        return f"Error reading the file: {e}"


# Example usage
file_name = "flag.txt"
file_content = read_file(file_name)
print(file_content)
