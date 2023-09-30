import pytest
import yaml
import requests


with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username':'SergeySA12', 'password': '2030224c72'})
    token = obj_data.json()['token']
    return token

@pytest.fixture()
def postP():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": my_dict['token']},data={
        'username':'SergeySA12',
        'password': '2030224c72',
        'title': 'newTitle',
        'description': 'AnythingNew',
        'content':'I sink you'})
    return obj_data.json()['description']