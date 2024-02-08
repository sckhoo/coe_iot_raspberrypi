from pydantic import BaseModel

class Payload(BaseModel):
    source : str
    temperature : float
    humidity : float
    sound : float
    light : float
    movement : float
    airquality: float
    interface_ip: str

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
