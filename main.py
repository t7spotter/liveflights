from flask import Flask
from icecream import ic
import requests
import http.client
import json

app = Flask(__name__)

@app.route("/<reg>")
def reg(reg):
    response = requests.get(f"https://www.jetphotos.com/api/json/lastseen.php?reg={reg}")
    response_json = response.json()
    result = response_json["result"]["response"]
    aircraft_info = result['aircraftInfo']
    flight_info = result['data']
    
    
    indexx = 0
    for index, live in enumerate(flight_info):
        if live['status']['live'] == True:
            indexx = index
    
    
    try:
        image = {"src":   result['aircraftImages'][0]['images']['large'][0]['src'],
             "copyright": result['aircraftImages'][0]['images']['large'][0]['copyright']}
    except:
        image = "Not available"
    
    try:        
        From = (f"{flight_info[indexx]['airport']['origin']['name']} \
                 [{flight_info[indexx]['airport']['origin']['code']['iata']}]")
    except:
        From = "Not available"
    
    try:        
        To = (f"{flight_info[indexx]['airport']['destination']['name']} \
               [{flight_info[indexx]['airport']['destination']['code']['iata']}]")
    except:
        To = "Not available"


    
    final_response = {
        "Image": image,
        "Index": indexx,
        "aircraft info":{
            "Registration":aircraft_info['registration'],
            "Airline": aircraft_info['airline']['name'],
            "Model": aircraft_info['model']['text'],
            "Country": aircraft_info['country']['name'],
        },
        "flight info": {
            "Is live": flight_info[indexx]['status']['live'],
            "From": From,
            "To": To,
            "Flight number": flight_info[indexx]['identification']['number']['default'], 
        }
    }
    return final_response