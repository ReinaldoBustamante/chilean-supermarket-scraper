from unidecode import unidecode
import re

def normalize_data(raw_name, rules, category):
    #print(rules["name_pattern"])
    clean_name = unidecode(raw_name).lower()

    name_pattern = rules["name_pattern"]
    pattern = rules["unit_pattern"]
    units_pattern = rules["amount_items_pattern"]
    
    quantity_value = int(re.search(pattern, clean_name).groups()[0]) if re.search(pattern, clean_name) else 1
    quantity_unit = re.search(pattern, clean_name).groups()[1] if re.search(pattern, clean_name) else ""
    units = int(re.search(units_pattern, clean_name).groups()[0]) if re.search(units_pattern, clean_name) else 1
    normalized_name = category + " " + " ".join(re.findall(name_pattern, clean_name)) if re.findall(name_pattern, clean_name) else category
   
    return {
        "normalized_name": normalized_name,
        "quantity_value": quantity_value,
        "quantity_unit": quantity_unit,
        "units": units
    }