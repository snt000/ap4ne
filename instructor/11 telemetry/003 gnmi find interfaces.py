from pygnmi.client import gNMIclient
from pprint import pprint
TARGET = ("devnetsandboxiosxec9k.cisco.com", 9339)
USER, PASS = "steveg", "7r_uz4_MOD2iW7"

with gNMIclient(target=TARGET, username=USER, password=PASS,
                insecure=False, skip_verify=True, timeout=10) as gc:
    #resp = gc.get(path=["interfaces"])
    resp = gc.get(path=["interfaces/interface/name"])
    
    pprint(resp)   # look for 'name' values like GigabitEthernet1 or GigabitEthernet1/0/1
