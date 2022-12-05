from Server import Server
def print_program_info():

    
    print("Server Automator v0.1 by Justin Ellis")

if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    my_server_ip = "54.189.51.103"
    my_rsa_key_file = r"C:\Users\khali\.ssh\JE_CNE"
    username = "ubuntu"
    my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'
    my_server = Server(my_server_ip, my_rsa_key_file, username, my_upgrade_command)
    print(my_server.ping())
    print("Updating server")
    ssh_result = my_server.upgrade()
    print(''.join(ssh_result))
    
    
    
