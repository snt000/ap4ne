from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir.core.filter import F

nr = InitNornir(config_file="config.yml")
#nr.inventory.hosts.keys()

Junos_devices = nr.filter(F(platform="junos"))
#print(Junos_devices.inventory.hosts.keys())

result = Junos_devices.run(task=napalm_get, getters=["facts"])
#print_result(result)
for item in Junos_devices.inventory.hosts:
   dev=nr.inventory.hosts[item]
   print("********device " + item + " ********")
   print(type(dev))
   print (dir(dev))
   print (dev.schema())
   print (dev.get("version"))
   print("expected version is " + dev['version']) 
   print("actual version is " + result[item][0].result["facts"]["os_version"])
   if dev['version'] == result[item][0].result["facts"]["os_version"]: 
     print ("the expected version is equal to the actual version")
   else: 
     print ("the expected version is not equal to the actual version")