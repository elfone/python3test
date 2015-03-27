#!/usr/bin/env python3
__author__ = 'Administrator'
import paramiko
#import os

hostname = '192.168.152.128'
port = 22
username = 'root'
pkey_file = '/home/root/.ssh/id_rsa'
dir_path = '/root/test'

if __name__ == '__main__':
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print('Retrieving {}'.format(f))
        sftp.get('/'.join([dir_path, f]), f)
#       sftp.get(os.path.join(dir_path, f). f)
    t.close()