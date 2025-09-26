from pygnmi.client import gNMIclient

#host = ('10.5.5.5', '57500')
#host = ('sandbox-iosxr-1.cisco.com', 9339)
host = ('devnetsandboxiosxec9k.cisco.com', 9339)

if __name__ == '__main__':
    #This one is TLS not plaintext but skips validation
    with gNMIclient(target=host, username='steveg', password='7r_uz4_MOD2iW7', insecure=False, skip_verify=True) as gc:
        #result = gc.get(path=['openconfig-interfaces:interfaces', 'openconfig-acl:acl'])
        result = gc.capabilities()

    print(result)
