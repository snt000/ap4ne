from ncclient import manager

#subsmsg=
#<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
#  <get>
#    <filter>
subsmsg="""
<config>
      <mdt-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-oper">
        <mdt-subscriptions/>
      </mdt-oper-data>
</config>
"""
#    </filter>
#  </get>
#</rpc>

mdt_subscription_request = """
    <filter>
        <sensor-subscription xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-oper?module=Cisco-IOS-XE-mdt-oper&revision=2020-07-01">
        </sensor-subscription>
    </filter>
    """

host="10.5.5.5"
with manager.connect(host=host, port=830,
								username="sntuser",
								hostkey_verify=False,
								password="Ilovenetworks99",
								device_params={'name':'iosxe'}) as m:
    device_caps = m.server_capabilities
    for cap in device_caps:
        if "mdt" in cap:
            print(cap)
    subs = m.get_config(mdt_subscription_request)
    print (subs.xml)
    