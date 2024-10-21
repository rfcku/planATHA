from score import calculate_match_score


def test_calculate_match_score():
    contacts = [{
        'contactID': 1,
        'name': 'John',
        'name1': 'Doe',
        'email': 'john@email.com',
        'postalZip': '12345',
        'address': '123 Main St, City, Country'
    },
    {
        'contactID': 2,
        'name': 'Jane',
        'name1': 'Doe',
        'email': 'ja@email.com',
        'postalZip': '1233456',
        'address': '4465 Some City'
    },
 {
        'contactID': 3,
        'name': 'Jane',
        'name1': 'Doe',
        'email': 'jane@email.com',
        'postalZip': '1233456',
        'address': 'a465 Main St, Country'
    }

    ]

    score, accuracy = calculate_match_score(contacts[0], contacts[0])
    assert score >= 80
    assert accuracy == 'High'

    score, accuracy = calculate_match_score(contacts[0], contacts[1])
    assert score <= 30 
    assert accuracy == 'Low'


