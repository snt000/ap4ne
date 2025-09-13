import time
def connect_and_fetch():
    #iterate over multiple devices
    #simulate send command and wait for command return
    #assume it takes 2 seconds for each device to establish connection and respond to your show commands
    time.sleep(2)
    print(f"Data saved for device {i}")
if __name__ == "__main__":
    TOTAL_DEVICES = 10
    start_time = time.time()
    for i in range(1, TOTAL_DEVICES+1):
        connect_and_fetch()
    print("--- %s seconds ---" % (time.time() - start_time))