import unittest
from app import client 
import requests, re
from bs4 import BeautifulSoup

def test_check_200():
    pages = ['/users_all' ,'/define-data', '/delete-data', '/add-data',  
             '/change-data']   
    for i in pages:
        res = client.get(i)
    
        assert res.status_code == 200

def test_define_data():
    url = "http://3.142.92.23:5000/define-data"

    data = {"id": 15}

    response = requests.post(url, data=data)
    a = response.text

    soup = BeautifulSoup(a, 'html.parser')

    items = soup.find_all('div', class_='h-100 p-5 bg-light border rounded-3')
    items = str(items).split('<p>')
    items = items[1].split("-")
    item = items[1]
    item = int(re.sub('</p>', '', item))

    if item == data.get('id'):
        print("test passed", item)

    else:
        print ("error")


def test_add_data():
    url = "http://3.142.92.23:5000/add-data"

    data = {"first_name" : "test", "second_name": "test"}

    r = requests.post(url, data=data)
    
    if r.status_code != 200:
        print("Adding item failed")
    else:
        print("Seccessfully added item to DB")



def test_delete_data():

    url = "http://3.142.92.23:5000/users_all"

    response = requests.get(url)
    a = response.text

    soup = BeautifulSoup(a, 'html.parser')
    items = soup.find_all('div', class_='h-100 p-5 bg-light border rounded-10')

    item = str(items).split('<p>')
    item = item[-4].split("-")
    item = item[1]
    item = int(re.sub('</p>', '', item))

    url_to_del = "http://3.142.92.23:5000/delete-data"

    data = {"id": item}
    request_del = requests.post(url_to_del, data=data)

    if request_del.status_code != 200:
        print("Error while deleting item")
    else:
        print("Deleting is completed!")



