from scrapli.driver.core import IOSXEDriver

my_device = {
    "host": "10.99.99.11",
    "auth_username": "sntuser",
	"auth_password": "Ilovenetworks99",
    "auth_secondary": "cisco",
    "auth_strict_key": False
}

with IOSXEDriver(**my_device, transport="ssh2") as conn:
    conn.send_configs(["interface loopback123", "description configured by scrapli"])