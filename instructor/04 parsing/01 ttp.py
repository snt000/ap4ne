from ttp import ttp
with open ("r1.cfg") as f:
    data_to_parse = f.read()
"""
interface Loopback0
 description Router-id-loopback
 ip address 192.168.0.113/24
!
interface Vlan778
 description CPE_Access_Vlan
 ip address 2002::fd37/124
 ip vrf CPE1
!
"""
ttp_template = """
hostname {{ hostname }}
username {{ username }} privilege 15 password 0 Ilovenetworks99
"""
"""
 ip address {{ ip }}/{{ mask }}
 description {{ description }}
 ip vrf {{ vrf }}
"""
# create parser object and parse data using template:
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()
#print (dir(parser))
# print result in JSON format
results = parser.result(format='json')[0]
print(results)