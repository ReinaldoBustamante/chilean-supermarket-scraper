from unidecode import unidecode
import re

def normalize_milk(raw_name):
    clean_name = unidecode(raw_name).lower()

    pattern = r'(\d+)\s*(l|litros?|ml|mililitros?|cc)'
    units_pattern = r'pack\s*(\d+)\s*un'
    name_pattern = r"semi\s*descremada|descremada|entera|light|sin\s*lactosa|natural|chocolate|vainilla|fresa|frutilla"
    
    quantity_value = int(re.search(pattern, clean_name).groups()[0]) if re.search(pattern, clean_name) else 1
    quantity_unit = re.search(pattern, clean_name).groups()[1] if re.search(pattern, clean_name) else ""
    units = int(re.search(units_pattern, clean_name).groups()[0]) if re.search(units_pattern, clean_name) else 1
    normalized_name = "leche " + " ".join(re.findall(name_pattern, clean_name)) if re.findall(name_pattern, clean_name) else "leche"
   
    return {
        "normalized_name": normalized_name,
        "quantity_value": quantity_value,
        "quantity_unit": quantity_unit,
        "units": units
    }
    
