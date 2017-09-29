# -*- coding:utf-8 -*-
__author__ = 'yang.tian'
import paramiko
from nt import chdir
import datetime

'''
filename= 'manage.py'
sh = paramiko.Transport(('10.32.20.23', 2222))
sh.connect(username = 'winit', password = '"G#HKn+V+&HwFr%6^')
sftp = paramiko.SFTPClient.from_transport(sh)
localpath = ('D:\workspace\earnMoney\{0}'.format(filename))
targetpath = ('/usr/local/winit_attendance/{0}'.format(filename))
sftp.put(localpath, targetpath)
sh.close()


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.32.20.23', port=2222, username='winit',password='"G#HKn+V+&HwFr%6^',allow_agent=True)
#ssh.connect('172.16.3.207', port=22, username='root',password='winit2015',allow_agent=False)
print ssh
comm = 'su root Aiw4ipH3EbxpXNKCKk'
stdin,stdout,stderr = ssh.exec_command(comm)
results=stdout.read()
print results
ftp = ssh.open_sftp()
filename = 'manage.py'
localpath = ('D:/workspace/earnMoney/{0}'.format(filename))
targetpath = ('/usr/local/winit_attendance/{0}'.format(filename))
ftp.put(localpath, targetpath)
ssh.close()
'''

print datetime.datetime.now()