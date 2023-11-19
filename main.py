from flask import Flask, request
from icecream import ic
import requests
import http.client
import json

app = Flask(__name__)

@app.route("/reg/<reg>")
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
    list_keys_of_dict = list(keys_of_dict)
    
    data_dict.pop('full_count', None)
    data_dict.pop('stats', None)
    data_dict.pop('version', None)
    
    def fetch_zone():
        url_bound = str(request)
    
        start_index = url_bound.find('/zone/') + len('/zone/')
        end_index = url_bound.find("'", start_index)

        coordinates_str = url_bound[start_index:end_index]
        coordinates = [float(coord) for coord in coordinates_str.split(',')]
        json_cordinate = {
            "x1": coordinates[0],
            "y1": coordinates[2],
            "x2": coordinates[1],
            "y2": coordinates[3],
        }
        return json_cordinate

    result = []

    




@app.route('/weather/<iata>')
def weather(iata):
    response = http.client.HTTPSConnection("api.flightradar24.com")
    response.request("GET", f"/common/v1/airport.json?code={iata}")
    res = response.getresponse()
    data = res.read()
    data_dict = json.loads(data)
    
    weather = data_dict['result']['response']['airport']['pluginData']['weather']
    return weather



if __name__ == '__main__':
    app.run(debug=True)