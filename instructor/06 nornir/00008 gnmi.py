from pygnmi.client import gNMIclient
from nornir import InitNornir
from nornir.core.task import Task, Result
import logging

# User-defined tasks
def gnmi_capabilites(task: Task) -> Result:
    with gNMIclient(target=(task.host.hostname, task.host.port), username=task.host.username,
                    password=task.host.password, insecure=True) as gc:
        r = gc.capabilities()
    return Result(host=task.host, result=r)
def gnmi_get(task: Task, path) -> Result:
    with gNMIclient(target=(task.host.hostname, task.host.port), username=task.host.username,
                    password=task.host.password, insecure=True) as gc:
        r = gc.get(path=path)
    return Result(host=task.host, result=r)

if __name__ == "__main__":
    nr = InitNornir(config_file='config.yml')
    dev = nr.filter(name="c1")
    result = dev.run(task=gnmi_capabilites)
    #result2 = dev.run(task=gnmi_get, path=['openconfig-interfaces:interfaces'])
    result2 = dev.run(task=gnmi_get, path=['process-cpu-ios-xe-oper:cpu-usage'])
    #print(result2['c1'][0])
    print(result)
    print(result["c1"])
    print(result["c1"][0])
    print(result2)
