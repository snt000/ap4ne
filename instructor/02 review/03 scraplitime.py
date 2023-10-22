from scrapli.driver.core import IOSXEDriver

my_device = {
    "host": "10.99.99.11",
    "auth_username": "sntuser",
	"auth_password": "Ilovenetworks99",
    "auth_strict_key": False
}
with IOSXEDriver(**my_device, transport="ssh2") as conn:
	print("Gathering 'show run'!")
	show_run_response = conn.send_command(command="show run")
	print(f"Show run complete in {show_run_response.elapsed_time} seconds, successful: {not show_run_response.failed}")

	print("Gathering 'show tech'!")
	show_tech_response = conn.send_command(command="show tech")
	print(f"Show run complete in {show_tech_response.elapsed_time} seconds, successful: {not show_tech_response.failed}")
	print(f"Show tech was {len(show_tech_response.result.splitlines())} lines long!! AHHHHHHHH!!!!")