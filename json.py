import json
print('Interface Status')
print('================================================================================')
print('DN                                              Description     Speed    MTU  ')
print('----------------------------------------------- --------------  ------  ------')
file = open('sample.json', 'r')
data = json.loads(file.read())
for i in data["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"],"                   ", i["l1PhysIf"]["attributes"]["speed"], " ", i["l1PhysIf"]["attributes"]["mtu"])