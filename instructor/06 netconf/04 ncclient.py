from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

"""
router = { "host": "sandbox-iosxe-recomm-1.cisco.com",
          "port": 830, 
          "username": "developer", 
          "password": "lastorangerestoreball8876" }

          m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)
"""
m = manager.connect(host="10.5.5.5", port=830, username="sntuser",
                    password="Ilovenetworks99", device_params={'name':'iosxe'}, hostkey_verify=False)

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
         <name>Loopback22</name>
      </interface>
   </interfaces>
</filter>
"""

running_config = m.get_config("running", netconf_filter)

running_config_xml = xmltodict.parse(running_config.xml)["rpc-reply"]["data"]
#pprint(running_config_xml["interfaces"]["interface"])
print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())
