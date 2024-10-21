from read_csv import read_contacts_from_csv

def test_read_csv():

    fileName = 'contacts.csv'

    # Read the CSV file
    data = read_contacts_from_csv(fileName)

    # Check the data
    assert data != None
    assert len(data) > 1


