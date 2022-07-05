import os
import paramiko
import sys

ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server=172.16.5.36 , username=username, password=password)
sftp = ssh.open_sftp()
sftp.put(f'F:\{sys.argv[1]}', 'remotepath')
sftp.close()
ssh.close()