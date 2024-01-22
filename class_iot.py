from pydantic import BaseModel

class Payload(BaseModel):
    temperature : float
    humidity : float
    sound : float
    light : float
    movement : float

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)