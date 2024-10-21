import time
from read_csv import read_contacts_from_csv
from find_duplicates import find_duplicate_contacts
import csv 

file_path = 'contacts.csv'  
contacts = read_contacts_from_csv(file_path)
print("Finding duplicates...")
start_time = time.time()
duplicates = find_duplicate_contacts(contacts)
end_time = time.time()
print(f"Found {len(duplicates)} possible duplicates in {end_time - start_time:.2f} seconds.")

# Write the duplicates to a new CSV file
def output_duplicates_to_csv(duplicates, output_file):
    """
    Writes the duplicate contacts into a CSV file.
    
    Args:
        duplicates (list): List of dictionaries containing the duplicates and their accuracy.
        output_file (str): Path to the output CSV file.
    """
    fieldnames = ['ContactID Source', 'ContactID Match', 'Accuracy']
    
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(duplicates)


output_duplicates_to_csv(duplicates, 'output.csv')
print("Duplicates written to 'duplicates.csv' file.")
