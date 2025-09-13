from nornir import InitNornir

# Initialise Nornir from config file
nr = InitNornir(config_file="config.yml")

print("### Exploring the main nr object ###")
print(type(nr))            # Nornir core object
print(dir(nr))             # Attributes & methods
print()

#obj = nr  # or host, or nr
obj = nr.inventory  # or host, or nr

for name in dir(obj):
    if name.startswith("__"):
        continue  # skip dunder methods to keep it clean
    attr = getattr(obj, name)
    if callable(attr):
        print(f"Method: {name}()")
    else:
        print(f"Attribute: {name}")
