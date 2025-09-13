from ncclient import manager
import xmltodict
import xml.dom.minidom

router = {
   'ip': '10.5.5.5',
   'port': '830',
   'username': 'sntuser',
   'password': 'Ilovenetworks99'
}

netconf_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
       <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
         <mdt-subscription>
         </mdt-subscription>
       </mdt-config-data>
    </filter>
"""

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

running_config = m.get_config('running', netconf_filter)

print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

m.close_session()