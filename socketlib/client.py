import socket
import os
from time import sleep

# Function to initialize the socket connection
def create_connection(host, port):
    print("Connecting...")
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        sleep(1)
        print("Connected OK!")
        return client_socket
    except socket.error as e:
        print(f"Connection failed: {e}")
        return None

# Function to change the directory on the client-side
def change_directory(client_socket, command, current_dir):
    client_socket.send(command.encode())
    data = client_socket.recv(1024).decode()
    print(data)

    # Update the local current directory if the change was successful
    if "Directory changed to" in data:
        current_dir = data.split("to ")[1].strip()
    
    return current_dir

# Function to handle user input and commands
def handle_commands(client_socket, current_dir):
    back = ["quit", "exit", "background"]
    while True:
        try:
            message = input(f"root@{current_dir}# ") 
            
            if message.lower().strip() in back:
                print("Exiting...")
                break
            
            if message.startswith("cd "):  
                current_dir = change_directory(client_socket, message, current_dir)
            elif message != "":
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print(data)
            else:
                print("Invalid Command. Please enter a valid command.")
        
        except socket.error:
            print("Socket error occurred. Retrying...")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    client_socket.close()

# Main function to start the program
def main():
    host = "127.0.0.1"
    port = 9999

    # Create the socket connection
    client_socket = create_connection(host, port)
    
    if client_socket:
        # Start the command handling loop
        current_dir = os.getcwd()  
        handle_commands(client_socket, current_dir)

if __name__ == "__main__":
    main()
