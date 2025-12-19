from unidecode import unidecode
import re

def normalize_data(raw_name, rules, category):
    #print(rules["name_pattern"])
    clean_name = unidecode(raw_name).lower()

    name_pattern = rules["name_pattern"]
    unit_pattern = rules["unit_pattern"]
    amount_items_pattern = rules["amount_items_pattern"]
    
    normalized_name = category + " " + " ".join(re.findall(name_pattern, clean_name)) if re.findall(name_pattern, clean_name) else category
    unit_value = int(re.search(unit_pattern, clean_name).groups()[0]) if re.search(unit_pattern, clean_name) else 1
    amount = int(re.search(amount_items_pattern, clean_name).groups()[0]) if re.search(amount_items_pattern, clean_name) else 1
    type_unit = re.search(unit_pattern, clean_name).groups()[1] if re.search(unit_pattern, clean_name) else ""

    return {
        "normalized_name": normalized_name,
        "amount": amount,
        "type_unit": type_unit,
        "unit_value": unit_value
    }