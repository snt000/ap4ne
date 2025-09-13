from ncclient import manager

c="""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback66</name>
            <description>Test2</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <enabled>true</enabled>
        </interface>
    </interfaces>
</config>
"""
def connect(host, user, password):
    with manager.connect(host=host,
            username=user,
            password=password,
            port=830,
            timeout=10,
            device_params = {'name':'junos'},
            hostkey_verify=False) as conn:

        conn.lock()

        # configuration as a text string
        host_name = """
        system {
            host-name foodi2-bar;
        }
        """
        send_config = conn.edit_config(format='text', config=host_name)
        print (send_config.tostring)

        #check_config = conn.validate()
        #print (check_config)

        compare_config = conn.compare_configuration()
        print (compare_config.tostring)

        conn.commit()
        conn.unlock()

connect ("10.5.5.4", "sntuser", "Ilovenetworks99")