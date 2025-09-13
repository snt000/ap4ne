from nornir import InitNornir

# Initialise Nornir from config file
nr = InitNornir(config_file="config.yml")

print("### Exploring the main nr object ###")
print(type(nr))            # Nornir core object
print(dir(nr))             # Attributes & methods
print()

print("### Exploring the inventory ###")
print(type(nr.inventory))  # Inventory object
print(dir(nr.inventory))   # Attributes & methods
print()

print("### Exploring hosts dictionary ###")
print(type(nr.inventory.hosts))   # dict
print(nr.inventory.hosts.keys())  # list of hostnames
print()

# Pick one host to explore in detail
first_host_name = list(nr.inventory.hosts.keys())[0]
host = nr.inventory.hosts[first_host_name]

print(f"### Exploring Host object: {first_host_name} ###")
print(type(host))          # Host object
print(dir(host))           # Attributes & methods
print()

print("### Host attributes ###")
print("hostname:", host.hostname)
print("platform:", host.platform)
print("username:", host.username)
print("groups:", host.groups)
print("data:", host.data)
print()

# ---- Pretty output for all hosts ----
print("### All hosts in inventory ###")
for name, h in nr.inventory.hosts.items():
    print(f"{name}: hostname={h.hostname}, platform={h.platform}, groups={[g.name for g in h.groups]}")
