# test_farmer_api.py
import json
import requests

url = "https://abcd1234.ngrok.io/predict_crop"  # use the Ngrok URL printed from server

input_data = {
    "soil_N": 20,
    "soil_P": 10,
    "soil_K": 30,
    "temperature": 35,
    "humidity": 50,
    "rainfall": 100
}

response = requests.post(url, data=json.dumps(input_data))
print(response.text)
