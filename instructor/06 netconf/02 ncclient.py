from ncclient import manager
import time

def connect(host, port, user, password):
    conn = manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            device_params = {'name':'junos'},
            hostkey_verify=False)

    result = conn.reboot()
    reboot_nodes = result.xpath('request-reboot-results/request-reboot-status')
    if reboot_nodes:
        reboot_time = result.xpath('request-reboot-results/request-reboot-status/@reboot-time')[0]
        if 'Shutdown NOW' in reboot_nodes[0].text:
            print ('Rebooted at:', time.ctime(int(reboot_time)))

connect("10.5.5.4", 830, "sntuser", "Ilovenetworks99")