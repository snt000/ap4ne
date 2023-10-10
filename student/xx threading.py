import threading  # import python's threading module
from netmiko import ConnectHandler
import time
import logging


csr1000v1 = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port' : 22,                # optional, defaults to 22
    'secret': 'C1sco12345',     # optional, defaults to ''
}
csr1000v2 = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port' : 22,
    'secret': 'C1sco12345',
}
iosxrv9000 = {
    'device_type': 'cisco_xr',
    'host':   'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port' : 22,
    'secret': 'C1sco12345',
}
nxosv9000 = {
    'device_type': 'cisco_nxos',
    'host':   'sandbox-nxos-1.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
    'port' : 22,
    'secret': 'Admin_1234!',
}


def connect_and_fetch(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show version', use_textfsm=True)
    print(net_connect.host)
    print("*" * len(net_connect.host))
    # print(output)


if __name__ == "__main__":
    threads = []
    all_devices = [csr1000v1, csr1000v2, iosxrv9000, nxosv9000]
    for device in all_devices:
        # Spawn threads and append to threads list
        th = threading.Thread(target=connect_and_fetch, args=(device,))
        threads.append(th)
    
    # iterate through threads list and start each thread to perform its task
    for thread in threads:
        thread.start()

    #Once all threads have done the work, join the output of all threads to return the final output.
    for thread in threads:
        thread.join()