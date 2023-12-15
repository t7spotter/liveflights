# Flight Tracker Web App

## Overview

This small web application, built with Flask, enables users to send requests in the form of URLs and receive JSON-formatted responses.

## Features

- **Zone-based Flight Tracking:** Utilize the web app to retrieve live information about active flights within a specified geographic range. Define the rectangular area by providing coordinates through the URL, and receive real-time details about the flights within that zone.

- **Retrieve Aircraft Information by Registration:** Get information about an aircraft based on its registration code.
  
- **Retrieve Weather Information by Airport IATA Code:** Fetch weather information about an airport based on its IATA code.
## Usage

### Zone-based Flight Tracking

1. Make a GET request to the `/zone/<zone>` endpoint, where `<zone>` represents the coordinates of two corners of a rectangle (e.g., `x1,x2,y1,y2`).

   Example:
    
    For example, in the image below, we want to track active flights in the sky over the Emirates. We define two points to specify the desired area (i.e., the green box), marked by the red dots.

    Each point has x and y, and you can specify them for any desired area. Enter these two points in the format x1, x2, y1, y2 at the end of the URL after `/zone/<x1,x2,y1,y2>`. Then, receive the response in `JSON` format.

    ![Emirates zone](https://github.com/t7spotter/liveflights/blob/main/images/UAE.png)

    In this case, each red dot represents a coordinate point (x, y), and the green box represents the specified zone of interest. You can use the x1, x2, y1, y2 values for any desired points or areas you want to track.

       `url:  http://your-host/zone/25.930446,23.992521,53.807891,56.809364`
```Response
         {
  "1 Zone": {
    "1 x": 25.930446,
    "1 y": 53.807891,
    "2 x": 23.992521,
    "2 y": 56.809364,
    "Cordinates": "25.930446, 53.807891 & 23.992521, 56.809364"
  },
  "2 Quantity": "56 Flights are on this zone.",
  "3 Flights": [
    {
      "1 Aircraft model": "A20N",
      "2 Registration": "A4O-OVG",
      "3 Register info": "http://localhost:5000/reg/A4O-OVG",
      "4 Origin": "DMM",
      "5 Origin weather": "http://localhost:5000/weather/DMM",
      "6 Destination": "MCT",
      "7 Dest weather": "http://localhost:5000/weather/MCT",
      "8 Live info": "http://localhost:5000/id/32e4d07e"
    },
.
.
.
```
### Retrieve Aircraft Information by Registration (Endpoint: /reg/<Aircraft_registration>):

By entering the aircraft registration, you can retrieve the following information:

Example:
    'url:  http://your-host/reg/A7-ALW`

```Response:
    Image:
        Copyright: Lorenz Kafenda
        Source (src): https://cdn.jetphotos.com/640cb/6/1943448_1698860351.jpg?v=0
    Aircraft Info:
        Airline: Qatar Airways
        Country: Qatar
        Model: Airbus A350-941
        Registration: A7-ALW
    Flight Info:
        Flight Number: QR1370
        From: Cape Town International Airport [CPT]
        Is Live: True
        To: Doha Hamad International Airport [DOH] 
```
This information includes details about the aircraft's image, copyright, airline, country, model, registration, flight number, departure airport (From), live status, and arrival airport (To).


### Retrieve Weather Information by Airport IATA Code (Endpoint: /weather/<Airport_iata_code>):

    By entering the airport IATA code, you can retrieve the following information:
Example:
    'url:  http://your-host/weather/LAX`
```Response:
    {
  "1 temp": {
    "celsius": 19,
    "fahrenheit": 66
  },
  "2 elevation": {
    "ft": 125,
    "m": 38
  },
  "3 humidity": 23,
  "4 pressure": {
    "hg": 30,
    "hpa": 1024
  },
  "5 sky_status": "Cloudy",
  "6 visibility": {
    "km": 16093000,
    "mi": 10,
    "nmi": 9
  },
  "7 wind": {
    "direction": {
      "degree": 80,
      "text": "From east"
    },
    "speed": {
      "kmh": 7,
      "kts": 4,
      "mph": 4,
      "text": "Calm"
    }
  }
}

```

