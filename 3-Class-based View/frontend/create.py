import requests
endpoint = "http://127.0.0.1:8000/api/create/"

data = {
    'title': 'book',
    'code':'book code updated'   
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())