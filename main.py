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


@app.route('/zone/<zone>')
def bound(zone):
    
    # Use this format in url "<zone>" for two corner of a rectangle to determine a zone: y1,y2,x1,x2
    # coordinates (y1, y2 ,x1, x2)
    
    bounds = zone.replace(",", "%2C")
    additional_params = "satellite=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=14400&gliders=1&stats=1"
       
    response = http.client.HTTPSConnection("data-cloud.flightradar24.com")
    response.request("GET", f"/zones/fcgi/feed.json?faa=1&bounds={bounds}&{additional_params}")
    res = response.getresponse()
    data = res.read()
    data_dict = json.loads(data)
    
    keys_of_dict = data_dict.keys()
    
    data_dict.pop('full_count', None)
    data_dict.pop('stats', None)
    data_dict.pop('version', None)
    
    ic(list(keys_of_dict))

    result = []
    result_reg = []
    info_reg = []

    
    for item in list(keys_of_dict):
        result.append([data_dict[item][8], data_dict[item][9], \
            "From", data_dict[item][11], "To", data_dict[item][12]])
        
    for item_reg in result:
        result_reg.append(item_reg[1])
    
    
    for register in result_reg:
        info_reg.append(reg(register))
        
    # live position info:  ################################# 
    list_keys_of_dict = list(keys_of_dict)
    flights_details_in_specific_bound = []
    for id in list_keys_of_dict:
        response = requests.get(f"https://data-live.flightradar24.com/clickhandler/?version=1.5&flight={id}")
        response_json = response.json()
        flights_details_in_specific_bound.append(response_json["trail"][0])
    ########################################################
    
    ic(result_reg)
    
    result_zip = list(zip(info_reg, flights_details_in_specific_bound))
    return result_zip