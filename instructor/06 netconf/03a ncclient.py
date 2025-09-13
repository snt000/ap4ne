from ncclient import manager

c="""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback99</name>
            <description>Test5</description>
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
            device_params = {'name':'iosxe'},
            hostkey_verify=False) as conn:

        send_config = conn.edit_config(c, target = 'running')
        print (send_config)

connect ("10.5.5.5", "sntuser", "Ilovenetworks99")