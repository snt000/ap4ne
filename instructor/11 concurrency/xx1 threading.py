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
    max_threads = 2 # Set max threads to 20. You can see what number works best for you.
    threads = []
    for device in [r11, r12, r13]:
        # Spawn threads and append to threads list
        th = threading.Thread(target=connect_and_fetch, args=(device,))
        threads.append(th)
        th.start()
        #After each thread is started and added to dictionary, we are checking if the total number
        #of threads is more than what we have configured. If yes, wait or else continue
        while True:
            alive_cnt = 0
            for t in threads:
                if t.is_alive():
                    alive_cnt += 1
            if alive_cnt >=max_threads:
                logging.info('Do not spawn new thread, already reached max limit of alive threads [%s]' % alive_cnt)
                time.sleep(2)
                continue
            break

    #Once all threads have done the work, join the output of all threads to return the final output.
    for thread in threads:
        thread.join()