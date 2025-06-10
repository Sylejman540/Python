contact_info = {
    "Kroni": "555-2432",
    "Rroni": "231-1245"
}

print(contact_info)

kroni_phone = contact_info["Kroni"]
print(kroni_phone)

#update values
contact_info["Rroni"] = "165-3212"
print(contact_info)

#add values
contact_info["Alina"] = "233-5321"
print(contact_info)

#delete values
del contact_info["Kroni"]
print(contact_info)

#keys() method
keys = contact_info.keys()
print(keys)

#values() method
values = contact_info.values()
print(values)

#items() method
items = contact_info.items()
print(items)