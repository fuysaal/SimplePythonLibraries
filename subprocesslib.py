import subprocess
import os

def run_command(command, save_to_file=False, file_name="output.txt"):
    """
    Runs the given command, captures the output, and prints it to the console.
    Optionally saves the output to a file.
    """
    try:
        # Run the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Print the output to the console
        print(f"Command Output:\n{result.stdout}")

        # If there is an error message, print it
        if result.stderr:
            print(f"Command Error Message:\n{result.stderr}")

        # Save the output to a file
        if save_to_file:
            with open(file_name, 'w') as f:
                f.write(result.stdout)
            print(f"Output has been saved to '{file_name}' file.")

    except subprocess.CalledProcessError as e:
        # If an error occurred during the command execution
        print(f"An error occurred while running the command. Error Code: {e.returncode}")
        print(f"Error Message: {e.stderr}")
    except Exception as e:
        # General error catch
        print(f"An unexpected error occurred: {e}")

# Get the command from the user
command = input("Please enter the command you want to run (e.g., ['echo', 'Hello, World!']): ")

# Ask if the user wants to save the output to a file
save_output = input("Do you want to save the output to a file? (Yes/No): ").lower()
save_to_file = save_output == "yes"
file_name = "output.txt"  # File name

# Run the command
run_command(command.split(), save_to_file, file_name)
