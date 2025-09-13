from ncclient import manager

def connect(host, port, user, pw):
    conn = manager.connect(host=host,
            port=port,
            username=user,
            password=pw,
            timeout=10,
            device_params = {'name':'junos'},
            hostkey_verify=False)


    result = conn.get_software_information('brief', test='me')
    print (type(result))
    print(dir(result))
    print ('Hostname:', result.xpath('software-information/host-name')[0].text)

connect("10.5.5.4", 830, "sntuser", "Ilovenetworks99")