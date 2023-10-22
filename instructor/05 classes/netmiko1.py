from netmiko import ConnectHandler

d = {
	'device_type': 'cisco_ios',
	'ip': '10.99.99.11',
	'username': 'sntuser',
	'password': 'Ilovenetworks99'
}

c1 = ConnectHandler(**d)
print(type(c1))
print(dir(c1))
output = c1.send_command('show ip interface brief')
print(output)