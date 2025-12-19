from santaisabel.milk.get_milk import get_milk
from santaisabel.flour.get_flour import get_flour
class SantaIsabelSpider:
    def __init__(self):
        self.name = "Santa Isabel"
        self.base_url = "https://www.santaisabel.cl"
    
    def run(self):
        print(f"--- Iniciando scraping en {self.name} ---")
        
        data_milk = get_milk()
        print(f"Resultados obtenidos de leche: {len(data_milk)} productos.")
        
        data_flour = get_flour()
        print(f"Resultados obtenidos de harina: {len(data_flour)} productos.")

        all_products = data_milk + data_flour 

        return all_products