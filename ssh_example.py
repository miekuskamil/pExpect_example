#!/usr/bin/python3

import pexpect
import re
import sys
import getpass
import subprocess

def newlines():
	print('\n')
	print('\n')
	print('---------------------------------------------------------------------------------------')
	print('\n---------------------------------------------------------------------------------------')
	print('\n---------------------------------------------------------------------------------------')
	print('\n---------------------------------------------------------------------------------------')
	print('\n')
	print('\n')


username = input('Username: ')
password = getpass.getpass()

child = pexpect.spawn('ssh -c aes256-cbc -l %s 192.168.0.254' % username)
child.logfile_read = sys.stdout.buffer

child.expect ('.*assword:.*')
child.sendline(password)
child.expect('.*#.*')

newlines()
child.sendline ('terminal length 0')
child.expect('.*#.*')

newlines()
child.sendline ('show version')
child.expect('.*#.*')

newlines()
child.sendline ('show ip int brief')
child.expect('.*#.*')

newlines()
child.sendline ('show run')
child.expect('.*#.*')

newlines()
subprocess.call("ls -la", shell=True)
newlines()

child.close()
