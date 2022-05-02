import requests

endpoint = "http://127.0.0.1:8000/search/"

get_response = requests.post(endpoint, json=
    {
   "user":1,
   "query":"blood7"
}
    )

print(get_response.json())