from nornir import InitNornir

nr = InitNornir("config.yml")

print ("Lists of all hosts in inventory:")
print (nr.inventory.hosts)