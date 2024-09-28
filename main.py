#This is a fitness tracker using Google Sheets
#OpenAI API and Nutritionix
#This is not filled out with my private information

import requests
from datetime import datetime
import os

#You could store these in Replit as well as this is sensitive data
GENDER = YOUR_GENDER
WEIGHT_KG = YOUR_WEIGHT
HEIGHT_CM = YOUR_HEIGHT
AGE = YOUR_AGE

#These are the ID and Key for Nutritionix stored in Replit
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
#This is the Sheety bearer stored in Replit
Bearer = os.environ["NT_BEARER"]

#Get exercise stats with Natural Language Query
exercise_endpoint = "https://trackapi.nutrtionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

#Save data into Google Sheets

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#Authenticate your Sheety API
#Get a bearer auth from Sheety
#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {os.environ['Token']}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
#Test
print(sheet_response.text)


