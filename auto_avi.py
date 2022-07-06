import os
import paramiko
import sys

# connect to ssh server
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='[ip]', username='[username]', password='[password]')
sftp = ssh.open_sftp()

local_folder= 'Enter folder path here'
remote_folder='Enter Desktop path here'+sys.argv[1]

# set working directory to remote folder
sftp.chdir(remote_folder)

remote_list = sftp.listdir('.')
local_list = os.listdir(local_folder)

for file in local_list:
    if file not in remote_list:
        sftp.put(local_folder+file, file)
        print(file+ ' was added.')

print('all done!')

sftp.close()
ssh.close()