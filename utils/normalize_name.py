from unidecode import unidecode
def normalize_name(raw_name):
    normalized_name = unidecode(raw_name).lower()
    return normalized_name



"""
    normalized_name: Leche Semidescremada sin lactosa chocolate 
    category: leche
    brand: soprole
    quantity_value: 1000
    quantity_unit: ml
    units: 2
"""