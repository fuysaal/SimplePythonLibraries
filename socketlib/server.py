import socket
import subprocess
import os
from time import sleep

# Function to handle directory change command
def change_directory(data, current_dir):
    """ Handle the 'cd' command and change the directory """
    dir_path = data[3:].strip()  
    try:
        new_dir = os.path.abspath(dir_path)  
        if os.path.isdir(new_dir):  
            os.chdir(new_dir)  
            current_dir = os.getcwd()  
            response_data = f"Directory changed to {current_dir}".encode()
        else:
            response_data = f"{new_dir} is not a valid directory".encode()
    except Exception as e:
        response_data = f"Error: {str(e)}".encode()

    return response_data, current_dir

# Function to execute commands
def execute_command(data):
    """ Execute a command using subprocess and capture the output """
    result = subprocess.run(data, capture_output=True, shell=True)
    if result.stdout.strip():  
        response_data = result.stdout
    else:
        response_data = "Command Executed..".encode()

    return response_data

# Function to handle client connection
def handle_client_connection(conn):
    """ Handle the client-server interaction """
    current_dir = os.getcwd()  
    while True:
        data = conn.recv(1024).decode()

        if not data:  
            print("Client disconnected.")
            break

        if data.startswith("cd "):  
            response_data, current_dir = change_directory(data, current_dir)
        else:
            response_data = execute_command(data)

        conn.send(response_data)  

# Function to set up server and accept connections
def setup_server(host, port):
    """ Set up server, listen for incoming connections and handle clients """
    print("Listening...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Waiting for a connection on {host}:{port}...")
    conn, address = server_socket.accept()
    print(f"Connected OK! Connected From >> {address}")

    return conn

# Main function to start the server
def main():
    host = "127.0.0.1"
    port = 9999
    conn = setup_server(host, port)
    handle_client_connection(conn)
    conn.close() 

if __name__ == "__main__":
    main()
