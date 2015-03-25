#!/usr/bin/env python3
import poplib
__author__ = 'Administrator'

username = 'abc'
password = '123456'

mail_server = 'pop.163.com'

p = poplib.POP3(mail_server)
p.user(username)
p.pass_(password)
temp = p.list()
for msg_id in range(1, len(p.list()[1])):
    print(msg_id)
    outf = open('{}.eml'.format(msg_id), 'wb')
    outf.write(b'\n'.join(p.retr(msg_id)[1]))
    outf.close()
p.quit()
