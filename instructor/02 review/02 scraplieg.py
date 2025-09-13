from scrapli.driver.core import IOSXEDriver

MY_DEVICE = {
	"host": "10.99.99.11",
	"auth_username": "sntuser",
	"auth_password": "Ilovenetworks99",
	"auth_secondary": "cisco",
	"auth_strict_key": False,
}
"""
MY_DEVICE = {
	"host": "sandbox-iosxe-recomm-1.cisco.com",
	"auth_username": "developer",
	"auth_password": "lastorangerestoreball8876",
	"auth_strict_key": False,
}
"""
"""
CSR1000V Host: 
SSH Port: 22
NETCONF Port: 830
RESTCONF Ports: 443 (HTTPS)
Username: developer
Password: lastorangerestoreball8876
"""
with IOSXEDriver(**MY_DEVICE, transport="ssh2") as conn:
# Platform drivers will auto-magically handle disabling paging for you
	result = conn.send_command("show ver")
	print(result.result)
