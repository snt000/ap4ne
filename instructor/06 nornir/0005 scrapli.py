from nornir_scrapli.tasks import get_prompt, send_command, send_commands, send_configs
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yml")
i = nr.filter(F(groups__contains="iosv"))

cmd_result = i.run(task=send_command, command="show ip int brief")
cmd_results = i.run(task=send_commands, commands=["show version", "show ip int brief"])

d = 'Configured by Scrapli through Nornir'
cfg_results = i.run(task=send_configs, configs=["interface fa3/0", f"description {d}"])
print_result (cmd_result)
print_result (cmd_results)
