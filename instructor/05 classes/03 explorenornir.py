from nornir import InitNornir
from explore import explore

nr = InitNornir(config_file="config.yml")

explore(nr, "nr")                  # main Nornir object
explore(nr.inventory, "inventory") # inventory
explore(nr.inventory.hosts, "hosts dict")

# Explore a single host
first_host = list(nr.inventory.hosts.values())[0]
explore(first_host, f"host: {first_host.name}")