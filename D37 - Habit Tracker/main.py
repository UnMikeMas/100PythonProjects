import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "api_token"
USER = "unmikemas"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.now()
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
draw_endpoint = f"{graph_endpoint}/{graph_params['id']}"
post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}
# response = requests.post(url=draw_endpoint, json=post_params, headers=headers)
# print(response.text)

put_endpoint = f"{draw_endpoint}/{post_params['date']}"
put_params = {
    "quantity": "18"
}
# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

delete_endpoint = put_endpoint
requests.delete(url=delete_endpoint, headers=headers)