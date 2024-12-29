# import requests
# from bs4 import BeautifulSoup

# # URL of the page you want to scrape
# url = 'https://www.rossmann.de/de/'

# # Send an HTTP request to the website
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the content of the page using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
#     data = soup.find_all('div',{'class':'rm-category__section'})
#     for i in data:
#         links = i.find_all('a',{'class':'rm-siteselect__wrapper--product'})
#         print(links)


# # rm-category__banner-link
# # rm-category__banner-responsive-link
# # rm-category__banner-image swiper-lazy swiper-lazy-loaded

# # link = "https://www.rossmann.de/"+"/de/baby-und-spielzeug-oball-o-ball/p/0074451103405"

# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
# import requests
# from bs4 import BeautifulSoup

# baseurl = 'https://www.rossmann.de/de/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# r = requests.get('https://www.rossmann.de/de/baby-und-spielzeug/spielzeug/c/olcat2_19', headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# productlist = soup.find_all('div', class_='rm-tile-product')

# productlinks = []

# for item in productlist:
#     for link in item.find_all('a', href=True):
#         print(link['href'])
#         productlinks.append(baseurl + link['href'])


# print(len(productlinks))

# import requests
# from bs4 import BeautifulSoup

# # Base URL of the site
# baseurl = 'https://www.rossmann.de'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# # Fetch the main category page
# r = requests.get(f'{baseurl}/de/baby-und-spielzeug/spielzeug/c/olcat2_19', headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# # Extract product links
# productlist = soup.find_all('div', class_='rm-grid__content')
# productlinks = []

# for item in productlist:
#     for link in item.find_all('a', href=True):
#         href = link['href']
#         # Fix relative URLs
#         if href.startswith('/'):
#             href = baseurl + href
#         productlinks.append(href)

# # Deduplicate links
# productlinks = list(set(productlinks))

# # Extract product details
# products = []

# for link in productlinks[:10]:  # Limit to 10 products for demonstration
#     print(f"Processing: {link}")
#     product_response = requests.get(link, headers=headers)
#     product_soup = BeautifulSoup(product_response.content, 'lxml')

#     try:
#         name = product_soup.find('div', class_='rm-product__title').text.strip()
#     except AttributeError:
#         name = "N/A"

#     try:
#         price = product_soup.find('div', class_='rm-price').text.strip()
#     except AttributeError:
#         price = "N/A"

#     try:

#         brand = product_soup.find('div', class_='rm-product__brand').text.strip()
#     except AttributeError:
#         brand = "N/A"

#     products.append({
#         'name': name,
#         'price': price,
#         'brand': brand,
#         'link': link
#     })
# # print("AKAMAMAMAMAM",products)
# # Print product details
# for product in products:
#     print(f"Name: {product['name']}")
#     print(f"Price: {product['price']}")
#     print(f"Brand: {product['brand']}")
#     print(f"Link: {product['link']}")
#     print("-" * 40)





import requests
from bs4 import BeautifulSoup
import csv

# Base URL of the site
baseurl = 'https://www.rossmann.de'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Fetch the main category page
r = requests.get(f'{baseurl}/de/baby-und-spielzeug/spielzeug/c/olcat2_19', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# Extract product links
productlist = soup.find_all('div', class_='rm-grid__content')
productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        href = link['href']
        # Fix relative URLs
        if href.startswith('/'):
            href = baseurl + href
        productlinks.append(href)

# Deduplicate links
productlinks = list(set(productlinks))

# Extract product details
products = []

for link in productlinks[:10]:  # Limit to 10 products for demonstration
    print(f"Processing: {link}")
    product_response = requests.get(link, headers=headers)
    product_soup = BeautifulSoup(product_response.content, 'lxml')

    try:
        name = product_soup.find('div', class_='rm-product__title').text.strip()
    except AttributeError:
        name = "N/A"

    try:
        price = product_soup.find('div', class_='rm-price').text.strip()
    except AttributeError:
        price = "N/A"

    try:
        brand = product_soup.find('div', class_='rm-product__brand').text.strip()
    except AttributeError:
        brand = "N/A"

    products.append({
        'name': name,
        'price': price,
        'brand': brand,
        'link': link
    })

# Save data to CSV file
csv_file = 'products.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'price', 'brand', 'link'])
    writer.writeheader()  # Write header row
    for product in products:
        writer.writerow(product)  # Write product datsa

print(f"Data saved to {csv_file}")
