#initial
import requests
import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from favoriot import get_favoriot, post_favoriot
from sensors_input import get_temperature
from class_iot import Payload

load_dotenv()
FAVORIOT_URL=os.environ.get("FAVORIOT_URL")
FAVORIOT_URL_STREAM=os.environ.get("FAVORIOT_URL_STREAM")
FAVORIOT_APIKEY=os.environ.get("FAVORIOT_APIKEY")
DEVICE_DEVELOPER_ID=os.environ.get("DEVICE_DEVELOPER_ID")
STREAM_DEVELOPER_ID=os.environ.get("STREAM_DEVELOPER_ID")

        
payload=Payload(
    temperature=get_temperature(),
    humidity=get_temperature(),
    sound=get_temperature(),
    light=get_temperature(),
    movement=get_temperature()
)

print(payload.model_dump_json())
response = post_favoriot(payload)
if 200 <= response.status_code < 300:
    print(response.status_code)
    data = json.loads(response.text)
    print(data)
else:
    print("API call failed with error:", response.status_code, response.reason)

data = get_favoriot()
print(data['numFound'])

    