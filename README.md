# About

Spawn SSH shell to vendor of choice and send as-if-directly-loggeded-in SSH commands.
Tested with APIC, NX-OS, IOS etc.

# Deployment
***python3 ssh_example.py***. 

# Extract
```bash
pi@raspberrypi:~/pExpect_example $ python3 ssh_example.py
Username: kamil
Password:
Password:

amigomnemonik#



-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------




terminal length 0
amigomnemonik#



-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------




show version
Cisco IOS Software, 1841 Software (C1841-ADVIPSERVICESK9-M), Version 12.4(24)T6, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2011 by Cisco Systems, Inc.
Compiled Tue 23-Aug-11 00:44 by prod_rel_team

ROM: System Bootstrap, Version 12.4(13r)T, RELEASE SOFTWARE (fc1)

amigomnemonik uptime is 2 minutes
System returned to ROM by power-on
System image file is "flash:c1841-advipservicesk9-mz.124-24.T6.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 1841 (revision 7.0) with 119808K/11264K bytes of memory.
Processor board ID FCZ131572E2
2 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
DRAM configuration is 64 bits wide with parity disabled.
191K bytes of NVRAM.
62720K bytes of ATA CompactFlash (Read/Write)

Configuration register is 0x2102

amigomnemonik#



-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------




show ip int brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.0.254   YES NVRAM  up                    up
FastEthernet0/1            192.168.1.1     YES NVRAM  up                    down
NVI0                       192.168.0.254   YES unset  up                    up
SSLVPN-VIF0                unassigned      NO  unset  up                    up
Virtual-Access1            unassigned      YES unset  down                  down
Virtual-Template1          192.168.0.254   YES TFTP   down                  down
Tunnel0                    unassigned      YES NVRAM  up                    up
amigomnemonik#



-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------




show process cpu history

amigomnemonik   05:42:54 PM Thursday Jan 2 2020 UTC


    22          1111122222                         44444
    88     111111111133333               44444     11111     111
100
 90
 80
 70
 60
 50
 40                                                *****
 30 **                                             *****
 20 **               *****                         *****
 10 **          **********                         *****
   0....5....1....1....2....2....3....3....4....4....5....5....6
             0    5    0    5    0    5    0    5    0    5    0
               CPU% per second (last 60 seconds)


    4
    1
100
 90
 80
 70
 60
 50
 40 *
 30 *
 20 *
 10 #
   0....5....1....1....2....2....3....3....



-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------




total 56
drwxr-xr-x  3 pi pi  4096 Jan  2 16:57 .
drwxr-xr-x 23 pi pi  4096 Jan  2 15:55 ..
drwxr-xr-x  8 pi pi  4096 Jan  2 16:53 .git
-rw-r--r--  1 pi pi 35149 Jan  2 16:53 LICENSE.md
-rw-r--r--  1 pi pi   285 Jan  2 16:53 README.md
-rwxr-xr-x  1 pi pi  1571 Jan  2 16:57 ssh_example.py




-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------




pi@raspberrypi:~/pExpect_example $ 
```

# Misc
Can be turned into more interactive script with arguments (devices/commands) and reporting with Jinja.
