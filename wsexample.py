# from bs4 import BeautifulSoup
# import requests
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# # url="https://www.flipkart.com/search?q=smartwatch+round&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=smartwatch+round%7CSmart+Watches&requestId=245cbea7-ec65-4d1e-bde4-bd8fc8f81a4f&as-searchtext=smartwatch%20"

# url="https://www.flipkart.com/search?q=camera+dslr&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=camera+dslr%7CDSLR+%26+Mirrorless&requestId=83502fc4-06ec-409a-9c74-30899d37bb32&as-searchtext=cama"

# response = requests.get(url)

# htmlcontent = response.content

# soup = BeautifulSoup(htmlcontent,'html.parser')

# titles = []
# prices = []
# images = []



# for d in soup.find_all('div',attrs={'class': 'tUxRFH'}):
#     title = d.find('div',attrs={'class':'KzDlHZ'})
#     print(title)


# for d in soup.find_all('div',attrs={'class': '_1sdMkc LFEi7Z'}):
#     title = d.find('div',attrs={'class':'VU-ZEz'})
#     print(title)

    # price = d.find('div',attrs={'class':'Nx9bqj CxhGGd'})
    # print(price)
   
    # image = d.find('img',attrs={'class':'Nx9bqj CxhGGd'})
    # print(image.get('src'))
    
    # titles.append(title.string)
    # prices.append(price.string)
    # images.append(image.get('src'))
    
    # print(titles)
    # print(prices)
    # print(images)
    
    
    
from bs4 import BeautifulSoup
import requests

# Correct the HTML for parsing (optional)
soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="html.parser")
print(soup.prettify())

# URL for web scraping
url = "https://www.flipkart.com/search?q=camera+dslr&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=camera+dslr%7CDSLR+%26+Mirrorless&requestId=83502fc4-06ec-409a-9c74-30899d37bb32&as-searchtext=cama"

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, features="html.parser")

    titles = []
    prices = []
    images = []

    for d in soup.find_all('div', attrs={'class': 'tUxRFH'}):
        title = d.find('div', attrs={'class': 'KzDlHZ'})
        if title:
            titles.append(title.get_text(strip=True))  # Get title text
            print(title.get_text(strip=True))  # Print title

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
