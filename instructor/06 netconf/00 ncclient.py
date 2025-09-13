from ncclient import manager
host="10.5.5.4"
with manager.connect(host=host, port=830, 
								username="sntuser", 
								hostkey_verify=False,
								password="Ilovenetworks99", 
								device_params={'name':'junos'}) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)
