from src.santaisabel.base.spider import get_data

url = "https://www.santaisabel.cl/lacteos-huevos-y-congelados/leches/leche-liquida"
rules = {
    'name_pattern': r"semi\s*descremada|descremada|entera|light|sin\s*lactosa|natural|chocolate|vainilla|fresa|frutilla",
    'amount_items_pattern': r'pack\s*(\d+)\s*un',
    'unit_pattern': r'(\d+)\s*(l|litros?|ml|mililitros?|cc)'
}

def get_milk():
    return get_data(url, rules, "leche")