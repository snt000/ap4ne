from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

iosv_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '10.99.99.12',
	'username': 'sntuser',
	'password': 'Ilovenetworks99',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show ip interface brief')
print(output)