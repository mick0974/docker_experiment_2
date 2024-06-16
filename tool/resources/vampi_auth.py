import requests

base_url = "http://localhost:5001"
setup_url = base_url + "/createdb"
login_url = base_url + "/users/v1/login"

response1 = requests.get(setup_url)

headers = {"Content-Type": "application/json; charset=utf-8"}

body = {
    "username": "admin",
    "password": "pass1"
}

response = requests.post(login_url, json = body)

auth_output = {
    "name": "Authorization",
    "value": "Bearer " + response.json()["auth_token"],
    "in": "header",
    "timeout": 60,
    "description": "Administration token"
}

print('[' + str(auth_output).replace('\'', '"') + ']')