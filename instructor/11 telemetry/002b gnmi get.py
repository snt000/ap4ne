from pygnmi.client import gNMIclient
from pprint import pprint

host = ('devnetsandboxiosxec9k.cisco.com', 9339)

if __name__ == '__main__':
    with gNMIclient(target=host, username='steveg', password='7r_uz4_MOD2iW7', insecure=False, skip_verify=True) as gc:
             result = gc.get(path=['interfaces', 'acl'])

    pprint(result)