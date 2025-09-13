from pygnmi.client import gNMIclient

#host = ('10.5.5.5', '57500')
host = ('sandbox-iosxr-1.cisco.com', '57777')

if __name__ == '__main__':
    with gNMIclient(target=host, username='admin', password='C1sco12345', insecure=True) as gc:
        #result = gc.get(path=['openconfig-interfaces:interfaces', 'openconfig-acl:acl'])
        result = gc.capabilities()

    print(result)
