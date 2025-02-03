import requests
from bs4 import BeautifulSoup
import json


def getRotation():
    url = "https://runescape.wiki/w/Wilderness_Flash_Events"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    table = soup.find("table", class_="wikitable align-center-1 align-right-2 wfe-rotations")

    events = []
    if table:
        rows = table.find_all("tr", class_="table-bg-grey") + table.find_all("tr", class_="table-bg-yellow")
        
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 2:
                event_name = cols[0].get_text(strip=True, separator=" ")
                event_time = cols[1].get_text(strip=True)
                events.append({"event": event_name, "time": event_time})


    with open("current_rotation.json", "w") as json_file:
        json.dump(events, json_file, indent=4)


getRotation()
