import json 

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

with open('json/sample-data.json') as f:
    data = json.load(f)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
