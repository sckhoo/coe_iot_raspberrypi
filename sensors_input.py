import random

def get_temperature():
    return round(random.uniform(22,26), 2)

def get_humidity():
    return round(random.uniform(48,55), 2)

def get_sound():
    return round(random.uniform(20,26), 2)

def get_light():
    return round(random.uniform(70,85), 2)

def get_movement():
    return round(random.uniform(0,10), 2)

def get_airquality():
    return round(random.uniform(10,20), 2)