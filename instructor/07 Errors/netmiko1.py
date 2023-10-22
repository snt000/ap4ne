from netmiko import ConnectHandler
import logging

logging.basicConfig(filename="netmiko.log", level=logging.DEBUG)
logger=logging.getLogger("netmiko")

d = {
	'device_type': 'cisco_ios',
	'ip': '10.99.99.11',
	'username': 'sntuser',
	'password': 'Ilovenetworks99'
}

c1 = ConnectHandler(**d)
output = c1.send_command('show ip interfaces brief')
print(output)