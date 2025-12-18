from spiders.santaisabel.products.milk import get_milk_data

class SantaIsabelSpider:
    def __init__(self):
        self.name = "Santa Isabel"
        self.base_url = "https://www.santaisabel.cl"
    
    def run(self):
        print(f"--- Iniciando scraping en {self.name} ---")
        
        # Llamamos a la lógica específica de un producto
        data = get_milk_data()
        
        print(f"Resultados obtenidos: {len(data)} productos.")
        return data