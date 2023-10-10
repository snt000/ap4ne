import threading  # import python's threading module
from netmiko import ConnectHandler
import time
import logging
from nwdevices import *

def connect_and_fetch(device_data):
    net_connect = ConnectHandler(**device_data)
    output = net_connect.send_command('show version', use_textfsm=True)
    print(net_connect.host)
    print("*" * len(net_connect.host))
    print(output)

import concurrent.futures

if __name__ == "__main__":
    all_devices = [r11, r12,r13]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(connect_and_fetch, all_devices)
