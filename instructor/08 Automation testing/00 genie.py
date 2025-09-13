from genie import testbed
import pprint

# Load testbed file (YAML)
testbed = testbed.load('testbed.yaml')

# Pick a device by name
device = testbed.devices['r11']
device.connect()

# Run and parse command
output = device.parse('show version')

# Pretty-print the structured output
pprint.pprint(output)