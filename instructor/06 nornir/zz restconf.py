import requests
import json
from nornir import InitNornir
#from rich import print as rprint
from nornir_utils.plugins.functions import print_result

requests.packages.urllib3.disable_warnings()

nr = InitNornir(config_file="config.yml")
r = nr.filter(name="c1")

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

def restconf_configuration_nornir_example(task):
    module = "Cisco-IOS-XE-native:native/router/router-ospf/ospf"
    url = f"https://{task.host.hostname}:443/restconf/data/{module}"
    print (url)
    response = requests.get(url, headers=headers, auth=(f"{task.host.username}", f"{task.host.password}"), verify=False)
    task.host["data"] = response.json()
    result = task.host["data"]
    print(result)

r.run(task=restconf_configuration_nornir_example)
