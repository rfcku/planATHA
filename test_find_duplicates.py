from find_duplicates import find_duplicate_contacts
def test_duplicate_finder():
    # Test contacts list with clear duplicates
    test_contacts = [
        {'contactID': 1, 'name': 'John', 'name1': 'Doe', 'email': 'john.doe@example.com', 'postalZip': '12345', 'address': '123 Main St'},
        {'contactID': 2, 'name': 'Johnny', 'name1': 'Doe', 'email': 'john.doe@example.com', 'postalZip': '12345', 'address': '123 Main St'},
        {'contactID': 3, 'name': 'Jane', 'name1': 'Doe', 'email': 'jane.doe@example.com', 'postalZip': '12345', 'address': '123 Main St'}
    ]
    
    duplicates = find_duplicate_contacts(test_contacts)
    assert len(duplicates) == 1
    assert duplicates[0]['Accuracy'] == 'High'
    
    print("All tests passed!")
    
test_duplicate_finder()
