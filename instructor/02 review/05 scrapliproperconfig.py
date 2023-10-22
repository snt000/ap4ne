from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg

"""
device = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
    "platform": "cisco_iosxe"
}
"""

device = {
    "host": "10.5.5.5",
    "auth_username": "sntuser",
    "auth_password": "Ilovenetworks99",
    "auth_strict_key": False,
    "platform": "cisco_iosxe"
}

with open("myconfig", "r") as f:
    my_config = f.read()

with Scrapli(**device, transport="ssh2") as conn:
    cfg_conn = ScrapliCfg(conn=conn)
    cfg_conn.prepare()
    cfg_conn.load_config(config=my_config, merge=True)
    diff = cfg_conn.diff_config()
    print(diff.side_by_side_diff)
    cfg_conn.commit_config()
    cfg_conn.cleanup()
    