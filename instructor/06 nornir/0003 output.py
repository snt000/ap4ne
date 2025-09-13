from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli

nr = InitNornir(config_file="config.yml")
dev = nr.filter(name="devxrv1")
# dev.inventory.hosts
result = dev.run(task=napalm_get, getters=["interfaces", "facts", "get_bgp_config"])
print_result(result)

'''
>>> result['vMX1'][0].result["interfaces"]["ge-0/0/0"]['is_up']
True

>>> result['vMX1'][0].result["facts"]["os_version"]
'18.2R1.9'

>>> result['vMX1'][0].result["get_bgp_config"]['underlay']['neighbors']['192.168.1.1']['remote_as']
104

>>> result['vMX1'][0].result["get_bgp_config"]['underlay']['local_as']
101
'''