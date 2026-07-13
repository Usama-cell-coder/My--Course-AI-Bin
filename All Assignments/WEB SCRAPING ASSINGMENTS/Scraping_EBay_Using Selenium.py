from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

URL = "https://www.ebay.com/sch/i.html?_nkw=smartphone"

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(options=options)

driver.get(URL)

time.sleep(10)  # IMPORTANT: replace WebDriverWait for eBay stability

html = driver.page_source

if "Access Denied" in html or "Robot" in html:
    print("❌ eBay blocked the request (Access Denied / Bot detected)")
    driver.quit()
    exit()

products = driver.find_elements(By.CSS_SELECTOR, "li.s-item")

print("Products found:", len(products))

data = []

for p in products:
    try:
        title = p.find_element(By.CSS_SELECTOR, "h3.s-item__title").text
        if title.strip() == "" or "Shop on eBay" in title:
            continue

        url = p.find_element(By.CSS_SELECTOR, "a.s-item__link").get_attribute("href")

        img = p.find_element(By.CSS_SELECTOR, "img").get_attribute("src")

        data.append({
            "theme": title,
            "url": url,
            "img": img,
            "lines": "N/A",
            "author": "N/A"
        })
    except:
        continue

with open("ebay_final.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["theme","url","img","lines","author"])
    writer.writeheader()
    writer.writerows(data)

driver.quit()

print("Done. Records:", len(data))