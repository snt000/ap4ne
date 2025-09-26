from pygnmi.client import gNMIclient
import logging

# Enable debug logging (shows the gRPC/gNMI chatter)
logging.basicConfig(level=logging.DEBUG)

# Define the gNMI target (address and port of your router)
gnmi_target = ('devnetsandboxiosxec9k.cisco.com', 9339)

# Define the subscription request
subscription = {
    "subscription": [
        {
        #    "path": "process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds",
        #    "path": "components/component[name=Switch1]/cpu/utilization/state/instant",
        #    "path": "interfaces/interface[name=GigabitEthernet0/0]/state/oper-status",
            "path": "lldp/state/chassis-id",
            #"mode": "on_change",          # stream updates only when value changes
            "mode": "sample",          # periodic pushes
            "sample_interval": 5_000_000_000   # 5s heartbeat (ns) if supported
        }
    ],
    "origin": "openconfig",
    #    "use_aliases": False,
    "mode": "stream",       # continuous stream
 #   "encoding": "json_ietf" # cleaner output than "proto"
}

# Open gNMI client session
with gNMIclient(target=gnmi_target,
                username="steveg",
                password="7r_uz4_MOD2iW7",
                insecure=False,
                skip_verify=True,
                timeout=10) as client:

#    resp = client.get(path=["components/component[name=Switch1]/cpu/utilization/state"])
#    print(resp)
    # Start subscription
    telemetry_stream = client.subscribe(subscribe=subscription)

    # Process updates as they arrive
    for n, message in enumerate(telemetry_stream, start=1):
        print(f"\n--- Update #{n} ---")
        print(message)

        # demo: stop after 5 updates
        if n == 5:
            break
