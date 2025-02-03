import json
from datetime import datetime
from rotations import getRotation
from timezones import getTime 


getRotation()
current_time_str = getTime() 
current_time = datetime.strptime(current_time_str, "%H:%M")


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

print(f"Current time: {current_time.strftime('%H:%M')}")
print(f"Next event: {next_event[1]} at {next_event[0].strftime('%H:%M')}")
