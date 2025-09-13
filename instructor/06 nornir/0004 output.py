from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F

nr = InitNornir(config_file="config.yml")
Junos_devices = nr.filter(F(platform="junos"))
# print(Junos_devices.inventory.hosts.keys())

result = Junos_devices.run(task=napalm_get, getters=["bgp_neighbors"])
# print_result(result)
# result['vMX1'][0].result["bgp_neighbors"]["global"]["peers"]["192.168.1.1"]["is_up"]

for dev in Junos_devices.inventory.hosts:
  print ("****** " + dev + " *******")
  for item in result[dev][0].result["bgp_neighbors"]["global"]["peers"]:
    if result[dev][0].result["bgp_neighbors"]["global"]["peers"][item]["is_up"] == True: 
        print ("BGP session with " + item + " is Established")  
    else: 
        print ("BGP session with " + item + " is not Established")