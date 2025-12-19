from playwright.sync_api import sync_playwright
from santaisabel.utils.normalize_data import normalize_data

domain = "https://www.santaisabel.cl"

def get_data(url, rules, category):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        
    
        page.wait_for_selector("div.slides")
        page.wait_for_selector("button.page-number")
        page.click("button#onetrust-accept-btn-handler")

        total_pages = page.locator("button.page-number").count()
        slider = page.locator("div.slides")

        for num_page in range(1, total_pages + 1):
            btn = slider.locator('button.page-number', has_text=str(num_page))
            btn.click()
            page.wait_for_selector('div.shelf-content')
            page.wait_for_selector("div[data-cnstrc-item-name]")
            page.wait_for_timeout(500)

            shelf_content = page.locator('div.shelf-content')
            
            products = shelf_content.locator("div[data-cnstrc-item-name]").all()
            
            for product in products:
                product_raw_name = product.get_attribute("data-cnstrc-item-name")
                product_price = product.get_attribute("data-cnstrc-item-price")
                product_brand = product.locator('p.text-sm.text-gray-500.mb-1.h-9.md\\:h-auto').text_content()
                product_img_url = product.locator('div.principal-product-image').locator('img').first.get_attribute('src')
                product_url = domain + product.locator('a').first.get_attribute('href')
                normalized_milk = normalize_data(product_raw_name, rules, category)

                object = {
                    "normalized_name": normalized_milk['normalized_name'],
                    "category": category,
                    "brand": product_brand,
                    "quantity_value": normalized_milk['quantity_value'],
                    "quantity_unit": normalized_milk['quantity_unit'],
                    "units": normalized_milk['units'],
                    "img_url": product_img_url,
                    "product_url": product_url,
                    "price": int(product_price)
                }
                results.append(object)
        browser.close()
    return results