import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='34.209.138.165', username='ubuntu', key_filename='/home/ubuntu/.ssh/messi.pem')
my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'

stdin, stdout, stderr = ssh.exec_command('lsb_release -a')

for line in stdout.read().splitlines():
    print(line)

ssh.close()