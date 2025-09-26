from pygnmi.client import gNMIclient
from pprint import pprint

TARGET = ("devnetsandboxiosxec9k.cisco.com", 9339)
USER, PASS = "steveg", "7r_uz4_MOD2iW7"

with gNMIclient(target=TARGET, username=USER, password=PASS,
                insecure=False, skip_verify=True, timeout=10) as gc:
    resp = gc.get(path=["components"])
    print(resp)  # look for component names containing "CPU"

with gNMIclient(target=TARGET, username=USER, password=PASS,
                insecure=False, skip_verify=True, timeout=10) as gc:
    resp = gc.get(path=["interfaces"])
    pprint(resp)  # look for interface 'name' values, e.g. GigabitEthernet1

    r2 = gc.get(path=["interfaces/interface[name=Loopback100]/state/counters"])
    print("boooooooooooooooooooooooooooooooooooooooooooooooooo")
    pprint (r2)
