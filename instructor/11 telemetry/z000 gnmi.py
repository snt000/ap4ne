from pygnmi.client import gNMIclient
from pygnmi.proto import gnmi_pb2

def receive_gnmi_telemetry(server_address, username, password, paths):
    # Create a gNMI client
    c = gNMIclient(target=server_address, username=username, password=password)

    # Create a subscription request
    subscribe_request = gnmi_pb2.SubscribeRequest()
    
    for path in paths:
        sub = subscribe_request.subscribe.add()
        sub.path.elem.add().name = path

    # Subscribe to the telemetry stream
    for update in c.subscribe(subscribe_request):
        # Process the telemetry data in 'update'
        print(f"Received telemetry data: {update}")
        
if __name__ == '__main__':
    server_address = '10.5.5.5:57500'
    username = 'sntuser'
    password = 'Ilovenetworks99'
    # Define the paths you want to subscribe to, e.g., '/interfaces/interface[name=Ethernet1]/state/counters'
    paths = ['/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds']

    receive_gnmi_telemetry(server_address, username, password, paths)