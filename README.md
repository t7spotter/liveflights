# Flight Tracker Web App

## Overview

This small web application, built with Flask, enables users to send requests in the form of URLs and receive JSON-formatted responses.

## Features

- **Flight Tracking:** Utilize the web app to retrieve live information about active flights within a specified geographic range. Define the rectangular area by providing coordinates through the URL, and receive real-time details about the flights within that zone.

## Usage

### Zone-based Flight Tracking

1. Make a GET request to the `/zone/<zone>` endpoint, where `<zone>` represents the coordinates of two corners of a rectangle (e.g., `x1,x2,y1,y2`).

   Example:
    
    For example, in the image below, we want to track active flights in the sky over the city of Los Angeles. We define two points to specify the desired area (i.e., the green box), marked by the red dots.

    Each point has x and y, and you can specify them for any desired area. Enter these two points in the format x1, x2, y1, y2 at the end of the URL after `/zone/<x1,x2,y1,y2>`. Then, receive the response in `JSON` format.


    ![Los Angeles zone](https://github.com/t7spotter/liveflights/blob/main/images/LA%20bounds.png)

    In this case, each red dot represents a coordinate point (x, y), and the green box represents the specified zone of interest. You can use the x1, x2, y1, y2 values for any desired points or areas you want to track.

       `url:  http://your-host/zone/33.61,34.26,-117.10,-118.63`
    
### Retrieve Aircraft Information by Registration (Endpoint: /reg/<reg>):

    By entering the aircraft registration, you can retrieve the following information:
Example:
    'url:  http://your-host/reg/A7-ALW`
Response:
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

This information includes details about the aircraft's image, copyright, airline, country, model, registration, flight number, departure airport (From), live status, and arrival airport (To).





