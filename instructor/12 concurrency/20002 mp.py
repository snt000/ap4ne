import time
from multiprocessing import Pool
def connect_and_fetch(i):
    #iterate over multiple devices
    #simulate send command and wait for command return
    #assume it takes 2 second for each device to establish connection and respond to your show commands
    time.sleep(2)
    print(f"Data saved for device {i}")
if __name__ == "__main__":
    TOTAL_DEVICES = 10
    start_time = time.time()
    with Pool(processes=4) as pool:
        pool.map(connect_and_fetch, list(range(1, TOTAL_DEVICES+1)))
    print("--- %s seconds ---" % (time.time() - start_time))