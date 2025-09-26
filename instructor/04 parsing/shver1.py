#import ntc_templates
from netmiko import ConnectHandler

mytarget = {
	'device_type': 'juniper',
	'ip': '10.5.5.8',
	'username': 'sntuser',
	'password': 'Ilovenetworks99'
}

nc = ConnectHandler(**mytarget)
output = nc.send_command('show version')
print("Plain text output")
print(output)
print("Structured data")
output = nc.send_command('show version', use_textfsm=True)
print(output)