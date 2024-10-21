import csv
import difflib
import time
from rapidfuzz import fuzz
from concurrent.futures import ThreadPoolExecutor

from collections import defaultdict
from read_csv import read_contacts_from_csv
from score import calculate_match_score

def find_duplicate_contacts(contacts):
 
    duplicates = []
    email_groups = defaultdict(list)  
    name_groups = defaultdict(list)   
    

    for contact in contacts:
        email_groups[contact['email'].lower()].append(contact)
        name_groups["{} {}".format(contact['name'], contact['name1'])].append(contact)

    def process_group(group):
        local_duplicates = []
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                score, accuracy = calculate_match_score(group[i], group[j])
                local_duplicates.append({
                    'ContactID Source': group[i]['contactID'],
                    'ContactID Match': group[j]['contactID'],
                    'Accuracy': accuracy
                 })
        return local_duplicates

    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_group, group) for group in email_groups.values() if len(group) > 1]
        for future in futures:
            duplicates.extend(future.result())

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_group, group) for group in name_groups.values() if len(group) > 1]
        for future in futures:
            duplicates.extend(future.result())
    
    print("Found {} possible duplicates.".format(len(duplicates)))
    return duplicates


    



