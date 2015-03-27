#!/usr/bin/env python3
__author__ = 'Administrator'

import paramiko

hostname = '192.168.152.128'
port = 22
username = 'root'
password = '123456'

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())  # 不加这一句会出现paramiko.ssh_exception.SSHException: Server '192.168.152.128' not found in known_hosts
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print(stdout.read().decode())
    s.close()