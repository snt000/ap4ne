from nornir import InitNornir
from nornir.core.task import Task, Result
from netmiko import ConnectHandler

def netmiko_show(task: Task) -> Result:
    host = task.host
    device = {
        "device_type": host.platform,  # e.g. "cisco_ios"
        "host": host.hostname,
        "username": host.username,
        "password": host.password,
    }
    with ConnectHandler(**device) as conn:
        output = conn.send_command("show version")
    return Result(host=task.host, result=output)

nr = InitNornir(config_file="config.yml")
r = nr.run(task=netmiko_show)
for h, result in r.items():
    print(h, result[0].result)
