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


def checkInput():
    while True:
        IP = input('IP: ')
        USERNAME = input('Username: ')
        PASSWORD = getpass.getpass()
        try:
            if not all([IP, USERNAME, PASSWORD ]):
                raise ValueError
        except ValueError:
            print("Please enter an appropriate values!")
        else:
            IP_check = IP.split('.')
            if (len(IP_check) == 4) and (1 <= int(IP_check[0]) <= 223) and (int(IP_check[0]) != 127) and (int(IP_check[0]) != 169 or int(IP_check[1]) != 254) and (0 <= int(IP_check[1]) <= 255 and 0 <= int(IP_check[2]) <= 255 and 0 <= int(IP_check[3]) <= 255): 
                return IP, USERNAME, PASSWORD
            else:
                print("Wrong IP format, try again...")
                continue

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



def execute(*args):

    CHILD = pexpect.spawn('ssh -c aes256-cbc %s -l %s' % (args[0], args[1]))
    CHILD.logfile_read = sys.stdout.buffer

    CHILD.expect('.*assword:.*')
    CHILD.sendline(args[2])
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
 

if __name__ == "__main__":

    ip, username, password = checkInput()
    execute(ip, username, password)
