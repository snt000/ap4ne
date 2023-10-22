from scrapli.driver.core import IOSXEDriver

MY_DEVICE = {
	"host": "10.99.99.11",
	"auth_username": "sntuser",
	"auth_password": "Ilovenetworks99",
	"auth_strict_key": False,
}

with IOSXEDriver(**MY_DEVICE, transport="ssh2") as conn:
# Platform drivers will auto-magically handle disabling paging for you
	result = conn.send_command("show run")
	print(result.result)
