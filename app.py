import json
from datetime import datetime
from rotations import getRotation
from timezones import getTime
from win10toast import ToastNotifier
import time
while(True):
    getRotation()
    current_time_str = getTime() 
    current_time = datetime.strptime(current_time_str, "%H:%M")

    # Open and load the JSON file with event data
    with open("current_rotation.json", "r") as file:
        data = json.load(file)

    events = [(datetime.strptime(event["time"], "%H:%M"), event["event"]) for event in data]

    events.sort()


    next_event = None
    for event_time, event_name in events:
        if event_time >= current_time:
            next_event = (event_time, event_name)
            break


    if next_event is None:
        next_event = events[0]


    toaster = ToastNotifier()
    toaster.show_toast(
        "Wilderness Event",
        f"Current time: {current_time.strftime('%H:%M')}\nNext event: {next_event[1]} at {next_event[0].strftime('%H:%M')}",  # Message
        duration=10 
    )

    print(f"Current time: {current_time.strftime('%H:%M')}")
    print(f"Next event: {next_event[1]} at {next_event[0].strftime('%H:%M')}")
    #Currently have this running every 5 minutes. Early version. Will have user give input in the future for how often
    #They want to be reminded. 
    time.sleep(600)
    
