from src.santaisabel.milk.get_milk import get_milk

class SantaIsabelSpider:
    def __init__(self):
        self.name = "Santa Isabel"
        self.base_url = "https://www.santaisabel.cl"
    
    def run(self):
        print(f"--- Iniciando scraping en {self.name} ---")
        
        data = get_milk()
        print(f"Resultados obtenidos de leche: {len(data)} productos.")
        
        return data