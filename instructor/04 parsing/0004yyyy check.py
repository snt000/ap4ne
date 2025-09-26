from textfsm import clitable
import os, ntc_templates
from netmiko import ConnectHandler

mytarget = {
	'device_type': 'juniper',
	'ip': '10.5.5.8',
	'username': 'sntuser',
	'password': 'Ilovenetworks99'
}
nc = ConnectHandler(**mytarget)

raw = nc.send_command("show version")

templates_dir = os.environ.get("NET_TEXTFSM") or os.path.join(
    os.path.dirname(ntc_templates.__file__), "templates"
)

print("Templates dir:", templates_dir)

cli = clitable.CliTable("index", templates_dir)
attrs = {"Command": "show version", "Platform": "juniper_junos"}  # or juniper_junos
print("Attrs:", attrs)
cli.ParseCmd(raw, attrs)
print("Template used:", cli.TableName())
print("Headers:", list(cli.header))
print("Rows:", [list(r) for r in cli])

"""
output = nc.send_command('show version')
print("Plain text output")
print(output)
print("Structured data")
output = nc.send_command('show version', use_textfsm=True)
print(output)
"""