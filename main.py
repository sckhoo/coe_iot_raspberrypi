#initial
import requests
import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from favoriot import get_favoriot, post_favoriot
from sensors_input import get_temperature, get_humidity, get_sound, get_light, get_movement, get_airquality
from class_iot import Payload
from get_ip import get_ip_address

load_dotenv()
FAVORIOT_URL=os.environ.get("FAVORIOT_URL")
FAVORIOT_URL_STREAM=os.environ.get("FAVORIOT_URL_STREAM")
FAVORIOT_APIKEY=os.environ.get("FAVORIOT_APIKEY")
DEVICE_DEVELOPER_ID=os.environ.get("DEVICE_DEVELOPER_ID")
STREAM_DEVELOPER_ID=os.environ.get("STREAM_DEVELOPER_ID")
SOURCE=os.environ.get("SOURCE")

        
payload=Payload(
    source=SOURCE,
    temperature=get_temperature(),
    humidity=get_humidity(),
    sound=get_sound(),
    light=get_light(),
    movement=get_movement(),
    airquality=get_airquality(),
    interface_ip=get_ip_address()
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

    