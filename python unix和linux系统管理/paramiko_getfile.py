#!/usr/bin/env python3
__author__ = 'Administrator'
import paramiko
#import os

hostname = '192.168.152.128'
port = 22
username = 'root'
password = '123456'
dir_path = '/root/test'

if __name__ == '__main__':
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print('Retrieving {}'.format(f))
        sftp.get('/'.join([dir_path, f]), f)
#       sftp.get(os.path.join(dir_path, f). f)
    t.close()