import csv

def read_contacts_from_csv(file_path):
    """
    Reads contacts from a CSV file and returns them as a list of dictionaries.
    Each dictionary represents a contact.
    """
    contacts = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            contacts.append({
                'contactID': row['contactID'],
                'name': row['name'],
                'name1': row['name1'],
                'email': row['email'],
                'postalZip': row['postalZip'],
                'address': row['address']
            })
    return contacts
