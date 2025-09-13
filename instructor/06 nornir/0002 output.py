from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

def inventory_usernames(task):
    return Result(host=task.host, result=f"{task.host.name} username is {task.host.username}")
output = nr.run(task=inventory_usernames)

print (output)

print (output["r1"])