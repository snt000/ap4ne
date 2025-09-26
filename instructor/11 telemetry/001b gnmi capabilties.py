from pygnmi.client import gNMIclient
from pprint import pprint
import json

host = ("devnetsandboxiosxec9k.cisco.com", 9339)

with gNMIclient(target=host, username="steveg", password="7r_uz4_MOD2iW7",
                insecure=False, skip_verify=True) as gc:
    caps = gc.capabilities()

print("\n== Raw (pprint) ==")
pprint(caps, width=100)  # formats nested dicts/lists nicely

print("\n== Just the first 10 models (name@org:version) ==")
for m in caps["supported_models"][:10]:
    print(f"{m['name']}@{m['organization']}:{m['version']}")

print("\n== JSON pretty ==")
print(json.dumps(caps, indent=2))
