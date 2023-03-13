import requests
from datetime import datetime as dt


GENDER = "Male"
AGE = 23
WEIGHT_KG = 99
HEIGHT_CM = 186
API_ID = "api_id"
API_KEY = "api_key"
API_ENDPOINT= "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_GET_ENDPOINT = "https://api.sheety.co/endpoint_code"
SHEETY_POST_ENDPOINT = "https://api.sheety.co/endpoint_adress"
SHEETY_AUTH = {
    "Authorization": "Basic ___code___"
    }

headers={
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

nutrition_parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=API_ENDPOINT, json=nutrition_parameters, headers=headers)
result = response.json()

today = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")
for exercise in result["exercises"]:
    sheety_parameters = {
    "workout": {
        "date":today,
        "time": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
}
    sheety_response = requests.post(SHEETY_POST_ENDPOINT, json = sheety_parameters, headers=SHEETY_AUTH)
    print(sheety_response.text)
    