# Python program to scrape Amazon using Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

URL = "https://www.amazon.com/gp/browse.html?node=6563140011"

# Open browser
driver = webdriver.Chrome()
driver.get(URL)

time.sleep(5)  # wait for page to fully load

quotes = []  # same variable name

# Find main container (Amazon uses divs)
table = driver.find_element(By.TAG_NAME, "body")

# Loop through product blocks
rows = table.find_elements(By.XPATH, "//div[contains(@class,'a-carousel-card')]")

for row in rows:
    quote = {}

    # Product Title
    try:
        title = row.find_element(By.XPATH, ".//span")
        quote['theme'] = title.text
    except:
        quote['theme'] = "N/A"

    # Product URL
    try:
        link = row.find_element(By.XPATH, ".//a")
        quote['url'] = link.get_attribute("href")
    except:
        quote['url'] = "N/A"

    # Image
    try:
        img = row.find_element(By.XPATH, ".//img")
        quote['img'] = img.get_attribute("src")
    except:
        quote['img'] = "N/A"

    # Keep same logic (split like quotes site)
    try:
        alt_text = img.get_attribute("alt")
        parts = alt_text.split(" ")
        quote['lines'] = parts[0] if len(parts) > 0 else "N/A"
        quote['author'] = parts[1] if len(parts) > 1 else "N/A"
    except:
        quote['lines'] = "N/A"
        quote['author'] = "N/A"

    quotes.append(quote)

# Save CSV
filename = 'amazon_data.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

driver.quit()

print("Scraping completed successfully!")