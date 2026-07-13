# Python program to scrape Daraz using Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # ADD THIS FOR CHROMEDRIVER PATH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import csv

# URL for Daraz Pakistan Smartphones
URL = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"

# Configure Chrome options to avoid detection
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# ========== CHROMEDRIVER PATH - UPDATE THIS LINE ==========
# CHANGE THIS PATH to where your chromedriver.exe is located
CHROME_DRIVER_PATH = r"C:\Users\PMLS\Documents\GitHub\My-Course-AI-Bin\chromedriver.exe"  # <--- UPDATE THIS PATH

# Initialize ChromeDriver with your specified path
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get(URL)

# Wait for page to load
wait = WebDriverWait(driver, 15)
time.sleep(5)  # Additional static wait

products = []

# Scroll to load more products
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Find product containers
try:
    # Method 1: Using common Daraz product card classes
    product_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-qa-locator='product-item'], div[class*='product-card'], div[class*='BmheN'], div[class*='card-wrapper'], div[class*='item']")
    
    if not product_cards:
        # Method 2: Fallback selector
        product_cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'product')] | //div[contains(@class, 'item')] | //div[@data-qa-locator='product-item']")
    
    print(f"Found {len(product_cards)} product cards")
    
except Exception as e:
    print(f"Error finding product cards: {e}")
    product_cards = []

# Extract product information
for index, card in enumerate(product_cards[:50], 1):  # Limit to 50 products
    product = {}
    
    print(f"Processing product {index}...")
    
    # Product Name/Title
    try:
        # Multiple possible selectors for product title
        title_selectors = [
            ".//div[contains(@class, 'title')]//span",
            ".//div[contains(@class, 'name')]//span",
            ".//a[contains(@class, 'title')]",
            ".//div[contains(@class, 'product-title')]",
            ".//div[contains(@class, 'info')]//a"
        ]
        
        title = None
        for selector in title_selectors:
            try:
                title_elem = card.find_element(By.XPATH, selector)
                title = title_elem.text.strip()
                if title:
                    break
            except:
                continue
        
        product['product_name'] = title if title else "N/A"
    except:
        product['product_name'] = "N/A"
    
    # Product URL
    try:
        url_selectors = [
            ".//a[contains(@class, 'title')]",
            ".//a[contains(@href, 'product')]",
            ".//div[contains(@class, 'info')]//a"
        ]
        
        url = None
        for selector in url_selectors:
            try:
                url_elem = card.find_element(By.XPATH, selector)
                url = url_elem.get_attribute("href")
                if url:
                    break
            except:
                continue
        
        product['product_url'] = url if url else "N/A"
    except:
        product['product_url'] = "N/A"
    
    # Product Price
    try:
        price_selectors = [
            ".//span[contains(@class, 'price')]",
            ".//div[contains(@class, 'price')]//span",
            ".//span[contains(@class, 'currency')]",
            ".//span[contains(@class, 'product-price')]"
        ]
        
        price = None
        for selector in price_selectors:
            try:
                price_elem = card.find_element(By.XPATH, selector)
                price = price_elem.text.strip()
                if price:
                    break
            except:
                continue
        
        product['price'] = price if price else "N/A"
    except:
        product['price'] = "N/A"
    
    # Original Price (if discounted)
    try:
        original_price_elem = card.find_element(By.XPATH, ".//span[contains(@class, 'original-price')] | .//del")
        product['original_price'] = original_price_elem.text.strip()
    except:
        product['original_price'] = "N/A"
    
    # Discount Percentage
    try:
        discount_elem = card.find_element(By.XPATH, ".//span[contains(@class, 'discount')] | .//div[contains(@class, 'discount')]")
        product['discount'] = discount_elem.text.strip()
    except:
        product['discount'] = "N/A"
    
    # Rating
    try:
        rating_selectors = [
            ".//div[contains(@class, 'rating')]",
            ".//span[contains(@class, 'rating')]",
            ".//div[contains(@class, 'star')]"
        ]
        
        rating = None
        for selector in rating_selectors:
            try:
                rating_elem = card.find_element(By.XPATH, selector)
                rating = rating_elem.text.strip()
                if rating:
                    break
            except:
                continue
        
        product['rating'] = rating if rating else "N/A"
    except:
        product['rating'] = "N/A"
    
    # Number of Reviews/Sold
    try:
        review_selectors = [
            ".//span[contains(@class, 'review')]",
            ".//div[contains(@class, 'sold')]",
            ".//span[contains(@class, 'sold')]"
        ]
        
        reviews = None
        for selector in review_selectors:
            try:
                review_elem = card.find_element(By.XPATH, selector)
                reviews = review_elem.text.strip()
                if reviews:
                    break
            except:
                continue
        
        product['reviews_sold'] = reviews if reviews else "N/A"
    except:
        product['reviews_sold'] = "N/A"
    
    # Product Image URL
    try:
        img_selectors = [
            ".//img[contains(@class, 'product')]",
            ".//img[contains(@src, 'image')]",
            ".//img[contains(@alt, 'product')]"
        ]
        
        img_url = None
        for selector in img_selectors:
            try:
                img_elem = card.find_element(By.XPATH, selector)
                img_url = img_elem.get_attribute("src")
                if not img_url:
                    img_url = img_elem.get_attribute("data-src")
                if img_url:
                    break
            except:
                continue
        
        product['image_url'] = img_url if img_url else "N/A"
    except:
        product['image_url'] = "N/A"
    
    # Seller Name (if available)
    try:
        seller_elem = card.find_element(By.XPATH, ".//div[contains(@class, 'seller')] | .//span[contains(@class, 'store')]")
        product['seller'] = seller_elem.text.strip()
    except:
        product['seller'] = "N/A"
    
    # Location (if available)
    try:
        location_elem = card.find_element(By.XPATH, ".//div[contains(@class, 'location')] | .//span[contains(@class, 'loc')]")
        product['location'] = location_elem.text.strip()
    except:
        product['location'] = "N/A"
    
    # Add to list
    if product['product_name'] != "N/A":  # Only add if product name exists
        products.append(product)

print(f"\nSuccessfully scraped {len(products)} products")

# Save to CSV
filename = 'daraz_products.csv'
if products:
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = ['product_name', 'price', 'original_price', 'discount', 
                      'rating', 'reviews_sold', 'seller', 'location', 
                      'product_url', 'image_url']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for product in products:
            w.writerow(product)
    
    print(f"Data saved to {filename}")
else:
    print("No products were scraped. The website structure might have changed.")
    print("Saving debug information...")
    
    # Save page source for debugging
    with open('debug_page_source.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    print("Debug HTML saved to debug_page_source.html")

# Print sample of scraped data
print("\nSample of scraped data:")
for i, product in enumerate(products[:5], 1):
    print(f"\nProduct {i}:")
    print(f"  Name: {product['product_name'][:50]}...")
    print(f"  Price: {product['price']}")
    print(f"  Rating: {product['rating']}")
    print(f"  URL: {product['product_url'][:80]}...")

driver.quit()
print("\nScraping completed successfully!")