from pygnmi.client import gNMIclient

import logging
logging.basicConfig(level=logging.DEBUG)

# Define the gNMI target (address and port)
gnmi_target = ("10.5.5.5", 57500)

# Define the gNMI subscription details
subscription = {
    "subscription": [
        {
            "path": "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds",
            "mode": 1,  # ON_CHANGE
            "sample_interval": 5000000000,  # 5 seconds in nanoseconds
        }
    ]
}

# Create a gNMI client connection
with gNMIclient(target=gnmi_target, username="sntuser", password="Ilovenetworks99", insecure=True, timeout=10) as client:
    # Subscribe to telemetry data
    result = client.subscribe(subscription, encoding="proto")

    for update in result:
        for update in update.update:
            # Extract and process telemetry data
            path = update.update.path
            value = update.update.val
            print(f"Path: {path}")
            print(f"Value: {value}")