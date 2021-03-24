import httplib2 as http
import json
import requests
import csv
import numpy
import pandas as pd

apiKey = "eWlqdiW9eGAfniHlPn6xQg2kJASwu4wVdL8swjxnWfTIfZ96sh"
user = "api_key=" + apiKey
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}

def LinkSensors(filename):
    data_file = open(filename, 'w')
    csv_writer = csv.writer(data_file, delimiter=';', lineterminator='\n')

    locationList = GetLocations()

    for location in locationList:
        locationData = GetLocation(location["locationId"])
        building = locationData["building"]
        icMeterList = building["indoorClimate"]
        for icMeter in icMeterList:
            address = icMeter["name"]
            tempId = icMeter["temperature"]["cid"]

            params = []
            params.append(address)
            params.append(tempId)
            csv_writer.writerow(params)

        #deviceList = GetDevices(location["locationId"])
        #for device in deviceList:

def GetLocation(locationID):
    try:
        from urlparse import urlparse
    except ImportError:
        try:
            from urllib.parse import urlparse
        except ImportError:
            print("urlparse failed")

    uri = 'https://app.neogrid.dk/public/api/v1/locations/' + str(locationID)
    method = 'GET'
    body = ''

    h = http.Http()
    print('Getting location ' + str(locationID))
    try:
        target = urlparse(uri + '?' + user)
        response, content = h.request(target.geturl(), method, body, headers)

        if response.status == 200:
            data = json.loads(content)
            return data

        else:
            print(uri + " returned status " + response['status'])
    except response.content as msg:
        print(msg)

def GetDevices(locationID):
    try:
        from urlparse import urlparse
    except ImportError:
        try:
            from urllib.parse import urlparse
        except ImportError:
            print("urlparse failed")

    uri = 'https://app.neogrid.dk/public/api/v1/locations/' + str(locationID) + '/'
    path = "devices"
    method = 'GET'
    body = ''

    h = http.Http()
    print('Getting devices from location ' + str(locationID))
    try:
        target = urlparse(uri + path + '?' + user)
        response, content = h.request(target.geturl(), method, body, headers)

        if response.status == 200:
            data = json.loads(content)
            return data["devices"]

        else:
            print(uri + " returned status " + response['status'])
    except response.content as msg:
        print(msg)

def GetLocations():
    try:
        from urlparse import urlparse
    except ImportError:
        try:
            from urllib.parse import urlparse
        except ImportError:
            print("urlparse failed")

    uri = 'https://app.neogrid.dk/public/api/v1/'
    path = "locations"
    request = ""
    method = 'GET'
    body = ''

    h = http.Http()
    print('Getting locations from NeoGrid')
    try:
        target = urlparse(uri + path + '?' + request + '&' + user)
        response, content = h.request(target.geturl(), method, body, headers)

        if response.status == 200:
            data = json.loads(content)
            return data["locations"]

        else:
            print(uri + " returned status " + response['status'])
            return
    except response.content as msg:
        print(msg)