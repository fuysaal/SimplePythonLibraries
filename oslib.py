import os

def create_file(file_name, content):
    # Check if the file already exists
    if os.path.exists(file_name):
        print(f"{file_name} already exists.")
    else:
        try:
            # Create the file
            with open(file_name, "w") as file:
                file.write(content)
            print(f"{file_name} has been successfully created.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Show the current working directory
print("Current working directory:", os.getcwd())

# Define file name and content
file_name = "sample.txt"
content = "Writing a file with Python."

# Call the file creation function
create_file(file_name, content)
