from datetime import datetime
import pytz
from rotations import getRotation

def getTime():

    tz_eu = pytz.timezone("Europe/London")

    datetime_EU = datetime.now(tz_eu).strftime("%H:%M")

    
    return datetime_EU


