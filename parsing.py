import requests
import re
from bs4 import BeautifulSoup

url = "http://3.142.92.23:5000/define-data"

data = {"id": 15}

response = requests.post(url, data=data)


a = response.text
print (a)
print('--------------------------------------------')

soup = BeautifulSoup(a, 'html.parser')

items = soup.find_all('div', class_='h-100 p-5 bg-light border rounded-3')
items = str(items).split('<p>')
items = items[1].split("-")
item = items[1]
item = int(re.sub('</p>', '', item))

print(item, type(item))
print(data.get('id'))


if item == data.get('id'):
    print("test passed", item)

else:
    print ("error")
