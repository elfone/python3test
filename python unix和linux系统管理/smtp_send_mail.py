#!/usr/bin/env python3
__author__ = 'Administrator'

import smtplib

mail_server = 'localhost'
mail_sverver_port = 25
from_addr = 'test@example.com'
to_addr = 'bar@exmaple.com'

from_header = 'From: %s\r\n' % from_addr
to_header = 'To: %s\r\n\r\n' % to_addr
subject_header = 'Subject: noting interesting'

body = 'This is a  not-very-interesting email.'

email_message = '%s\n%s\n%s\n\n%s' % (from_header, to_header, subject_header, body)

s = smtplib.SMTP(mail_server, mail_sverver_port)
s.sendmail(from_addr, to_addr, email_message)
s.quit()