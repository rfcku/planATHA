import difflib


def calculate_match_score(contact1, contact2):
    """
    Calculate the match score between two contacts based on name, email, zip, and address.
    Returns a score and a match accuracy level.
    """
    score = 0
    
    # Email match (high importance)
    if contact1['email']:
        if contact1['email'].lower() == contact2['email'].lower():
            score += 100  # High weight for exact email match
    
    # First Name match
    if contact1['name'].lower() == contact2['name'].lower():
        score += 20

    # Last Name match
    if contact1['name1'].lower() == contact2['name1'].lower():
        score += 10

    # Zip Code match
    if contact1['postalZip'] == contact2['postalZip']:
        score += 10

    # Address match
    if contact1['address'] and contact2['address']:
        ratio = difflib.SequenceMatcher(None, contact1['address'], contact2['address']).ratio()
        if ratio > 0.85:  # High similarity
            score += 20
        elif ratio > 0.5:  # Moderate similarity
            score += 10
    
    # Define match accuracy based on score
    if score >= 70:
        return score, 'High'
    elif score >= 40:
        return score, 'Medium'
    else:
        return score, 'Low'
