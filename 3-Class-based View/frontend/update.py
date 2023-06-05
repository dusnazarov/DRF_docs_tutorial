# ///////////////////////////////////////
import requests

endpoint = "http://127.0.0.1:8000/api/7/update/"

data = {
    'title': 'book updated',
    'code':'book code updated'   
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())


    