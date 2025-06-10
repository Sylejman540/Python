# Basic contact list with phone numbers
phone_book = {
    "Lina": "555-2432",
    "Mark": "231-1245"
}

print(phone_book)

# Access Lina's phone number
lina_number = phone_book["Lina"]
print(lina_number)

# Update Mark's phone number
phone_book["Mark"] = "165-3212"
print(phone_book)

# Add a new contact Sara
phone_book["Sara"] = "233-5321"
print(phone_book)

# Remove Lina from the contacts
del phone_book["Lina"]
print(phone_book)

# Show all contact names
all_names = phone_book.keys()
print(all_names)

# Show all phone numbers
all_numbers = phone_book.values()
print(all_numbers)

# Show all contact entries (name and number pairs)
all_entries = phone_book.items()
print(all_entries)


# Detailed contact info with nested dictionaries
contacts = {
    "Mira": {
        "phone": "3234-1451",
        "email": "mira@gmail.com",
        "address": "1234 st",
        "birthday": "20/11/2004"
    },
    "Alex": {
        "phone": "1434-4455",
        "email": "alex@gmail.com",
        "address": "4345 st",
        "birthday": "02/05/1993"
    }
}

print(contacts)
print(contacts["Mira"])