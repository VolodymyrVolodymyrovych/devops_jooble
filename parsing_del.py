import requests
import re
from bs4 import BeautifulSoup

url = "http://3.142.92.23:5000/users_all"

response = requests.get(url)


a = response.text
print (a)
print('--------------------------------------------')



soup = BeautifulSoup(a, 'html.parser')

items = soup.find_all('div', class_='h-100 p-5 bg-light border rounded-10')
print(items, type(items))
print('--------------------------------------------')


item = str(items).split('<p>')
item = item[-4].split("-")
item = item[1]

item = int(re.sub('</p>', '', item))

print(item, type(item))




if item == data.get('id'):
    print("test passed", item)

else:
    print ("error")


