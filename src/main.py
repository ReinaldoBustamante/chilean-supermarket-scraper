from santaisabel.santa_isabel import SantaIsabelSpider
import json 
def main():
    si_spider = SantaIsabelSpider()
    products = si_spider.run()
    print(f"Total de productos obtenidos: {len(products)}")

    print(json.dumps(products, indent=2))
        
if __name__ == "__main__":
    main()