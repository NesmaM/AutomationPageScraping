from bs4 import BeautifulSoup
import requests
url = "https://scrapingclub.com/exercise/list_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='w-full rounded border')
count = 1
for i in items:
    itemName = i.find('h4').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
pages = soup.find('nav',class_='pagination')  
urls = []
links = pages.find_all('span', class_='page')
for link in links:
    for a in link.find_all('a', href=True):
        pageNum = int(a.text) if a.text.isdigit() else None
        if pageNum != None:
            pageNumLink = a['href']
#            print(pageNumLink)
            urls.append(pageNumLink)
#print(urls)
for i in urls: 
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')
    for i in items:
        itemName = i.find('h4').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1




