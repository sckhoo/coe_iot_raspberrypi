from dotenv import load_dotenv
from pydantic import BaseModel
import json
import os
import requests

load_dotenv()
FAVORIOT_URL=os.environ.get("FAVORIOT_URL")
FAVORIOT_URL_STREAM=os.environ.get("FAVORIOT_URL_STREAM")
FAVORIOT_APIKEY=os.environ.get("FAVORIOT_APIKEY")
DEVICE_DEVELOPER_ID=os.environ.get("DEVICE_DEVELOPER_ID")
STREAM_DEVELOPER_ID=os.environ.get("STREAM_DEVELOPER_ID")

def post_favoriot(payload):
    print(payload)
    payload = json.dumps({
        "device_developer_id": DEVICE_DEVELOPER_ID,
        "data": {
            "source":payload.source,
            "temperature":payload.temperature,
            "humidity":payload.humidity,
            "sound":payload.sound,
            "light":payload.light,
            "movement":payload.movement,
            "airquality":payload.airquality
            }
        })
    headers = {
        'apikey': FAVORIOT_APIKEY,
        'Content-Type': 'application/json'
        }
    try:
        response = requests.request("POST", FAVORIOT_URL, headers=headers, data=payload)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        return response 
    
def get_favoriot():
    payload = json.dumps({
        "device_developer_id": DEVICE_DEVELOPER_ID,
        })
    headers = {
        'apikey': FAVORIOT_APIKEY,
        'Content-Type': 'application/json'
        }
    try:
        response = requests.request("GET", FAVORIOT_URL_STREAM, headers=headers, data=payload)
        response.raise_for_status()
        if 200 <= response.status_code < 300:
            return(json.loads(response.text))
    except requests.exceptions.RequestException as e:
        return response 