from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = f'https://www.newegg.com/p/pl?d=graphics+card'

# Opens up connection grabbing d page
uClient = uReq(my_url)

# offloads d content into a variable
page_html = uClient.read()

# closes d client
uClient.close()

# calls bs4 fn to parse the file
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-cell"})

# saves file in csv format
filename = "graphics_card.csv"
f = open(filename, "w")

headers = "BRAND, PRODUCT NAME, SHIPPING\n"

f.write(headers)

# loops through each product in the container
for container in containers:
    # gets brand name
    links = container.findAll("a", {"class": "item-brand"})
    for link in links:
        brand = link.img["title"]

    # gets product name
    title_container = container.findAll("a", {"class": "item-title"})
    for title in title_container:
        product_name = title.text

    # gets shipping price
    shipping_container = container.findAll("li", {"class": "price-ship"})
    for shipping in shipping_container:
        if shipping.text == "":
            shipping_price = "Not Available"
        else:
            shipping_price = shipping.text.strip()

    f.write(brand + "," + product_name.replace(",", " |") + "," + shipping_price + "\n")


