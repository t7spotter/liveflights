# Flight Tracker Web App

## Overview

This small web application, built with Flask, enables users to send requests in the form of URLs and receive JSON-formatted responses.

## Features

- **Flight Tracking:** Utilize the web app to retrieve live information about active flights within a specified geographic range. Define the rectangular area by providing coordinates through the URL, and receive real-time details about the flights within that zone.

## Usage

### Zone-based Flight Tracking

1. Make a GET request to the `/zone/<zone>` endpoint, where `<zone>` represents the coordinates of two corners of a rectangle (e.g., `x1,x2,y1,y2`).

   Example:
    http://your-host/zone/36.5,33.68,49.2,54.43

/LA bounds.png
