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


if __name__ == "__main__":
    threads = []
    for device in [r11, r12, r13]:
        # Spawn threads and append to threads list
        t = threading.Thread(target=connect_and_fetch, args=(device,))
        threads.append(t)
        t.start()

    #Once all threads have done the work, join the output of all threads to return the final output.
    for thread in threads:
        thread.join()