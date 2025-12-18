from spiders.santaisabel.spider import SantaIsabelSpider
import json

def main():
    si_spider = SantaIsabelSpider()
    resultados = si_spider.run()
    print(json.dumps(resultados, indent=2))
        
if __name__ == "__main__":
    main()