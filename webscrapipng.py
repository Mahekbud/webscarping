from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

url="https://www.flipkart.com/search?q=smartwatch+round&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=smartwatch+round%7CSmart+Watches&requestId=245cbea7-ec65-4d1e-bde4-bd8fc8f81a4f&as-searchtext=smartwatch%20"

response = requests.get(url)
# print (response.status_code)
# print (response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find('a'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for image in soup.find_all('img'):
#     print(image.get('src'))

# product = soup.find_all('div',class_='WOvzF4')
# print(product);


# product = soup.find('div',attrs={'class':'WOvzF4'})
# print(product)