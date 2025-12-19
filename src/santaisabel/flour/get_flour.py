from santaisabel.base.spider import get_data

url = "https://www.santaisabel.cl/despensa/harinas-postres-y-reposteria/harina-blanca"

rules = {
    'name_pattern': r"con\s*polvos\s*de\s*hornear|sin\s*polvos\s*de\s*hornear",
    'amount_items_pattern': r'pack\s*(\d+)\s*un',
    'unit_pattern': r'(\d+)\s*(kg|kilogramos?|g|gramos?|)'
}

def get_flour():
    return get_data(url, rules, "harina")