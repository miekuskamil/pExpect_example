#!/usr/bin/python3

"""
General pExpect module example to present command extract.
It has been tested against Cisco ACI to ease command extract
which sometimes could be an enormous exercise
if we were to extract the same with i.e. Ansible and API calls.
The below presents extract and command run against/on my home Cisco router and Pi's Bash shell respectively.
"""

import sys
import getpass
import subprocess
import pexpect

def newlines():
    "Function to pretty add number of spearators"
    print('\n')
    print('\n')
    print('-------------------------------------------------------------------------------------')
    print('\n-------------------------------------------------------------------------------------')
    print('\n-------------------------------------------------------------------------------------')
    print('\n-------------------------------------------------------------------------------------')
    print('\n')
    print('\n')


USERNAME = input('Username: ')
PASSWORD = getpass.getpass()

CHILD = pexpect.spawn('ssh -c aes256-cbc -l %s 192.168.0.254' % USERNAME)
CHILD.logfile_read = sys.stdout.buffer

CHILD.expect('.*assword:.*')
CHILD.sendline(PASSWORD)
CHILD.expect('.*#.*')

newlines()
CHILD.sendline('terminal length 0')
CHILD.expect('.*#.*')

newlines()
CHILD.sendline('show version')
CHILD.expect('.*#.*')

newlines()
CHILD.sendline('show ip int brief')
CHILD.expect('.*#.*')

newlines()
CHILD.sendline('show process cpu history')
CHILD.expect('.*#.*')

newlines()
subprocess.call("ls -la", shell=True)
newlines()

CHILD.close()
