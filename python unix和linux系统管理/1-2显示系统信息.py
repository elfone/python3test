#!/usr/bin/env python3
# A system Information Gathering SCript
import subprocess

# Command 1
uname = "uname"
uname_arg = "-a"
print("Gathering system information with {} command:\n".format(uname))
subprocess.call([uname, uname_arg])

# Command 2
diskspcae = "df"
diskspcae_arg = '-h'
print("Gathering diskspace information {} command:\n".format(diskspcae))
