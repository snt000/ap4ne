from netmiko import ConnectHandler

l2 = {
    'device_type': 'cisco_ios', 'ip': '10.99.99.12', 'username': 'sntuser', 'password': 'Ilovenetworks99', 'secret': 'cisco' }

net_connect = ConnectHandler(**l2)

net_connect.enable()

config_commands = ['int loop 0', 'ip address 1.1.1.31 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

net_connect.save_config(cmd="write mem")