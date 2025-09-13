import time
import asyncio
async def connect_and_fetch(i):
    #iterate over multiple devices
    #simulate send command and wait for command return
    #assume it takes 2 second for each device to establish connection and respond to your show commands
    await asyncio.sleep(2)
    print(f"Data saved for device {i}")
async def main():
    coroutines = [connect_and_fetch(i) for i in range(1, TOTAL_DEVICES+1)]
    await asyncio.gather(*coroutines)
if __name__ == "__main__":
    TOTAL_DEVICES = 10
    start_time = time.time()
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))