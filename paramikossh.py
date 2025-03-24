import paramiko


def ssh_connect(host, port, username, password, command='uptime'):
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()

        # Automatically add the server's host key (to avoid manual verification)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server via SSH
        ssh_client.connect(host, port=port, username=username, password=password)

        print(f"Successfully connected to: {host}")

        # Execute the specified command (default is 'uptime')
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(f"Command Output: {stdout.read().decode()}")

        # Close the SSH connection
        ssh_client.close()

    except paramiko.AuthenticationException:
        print("Authentication failed, please check your username/password.")
    except paramiko.SSHException as e:
        print(f"SSH connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Get SSH details from the user
host = input("Enter the SSH server address (e.g., your.remote.server.com): ")
port = int(input("Enter the SSH port (default is 22): ") or 22)  # Default port is 22
username = input("Enter the SSH username: ")
password = input("Enter the SSH password: ")
command = input("Enter the command you want to execute (default is 'uptime'): ") or 'uptime'

# Establish the SSH connection and run the command
ssh_connect(host, port, username, password, command)
