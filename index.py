import requests
import json
import time
from operator import attrgetter
from random import randint
from base64 import b64encode

# This function retrieves the humidity value from the sensors.
def getHumidity():

    # Execute a HTTP GET request to the SAP IoT Service API.
    deviceId = 24
    url = 'https://96e9f7bd-c38b-458d-8b98-630be0232fb8.eu10.cp.iot.sap/iot/core/api/v1/devices/%s/measures?top=1&orderby=timestamp desc' % str(deviceId)
    headers = {'content-type': 'application/json', 'Authorization' : 'Basic YXR0ZW5kZWUuYWRtaW46V2VsY29tZTE='}
    r = requests.get(url, headers = headers, timeout=5)
    responseCode = r.status_code
    data = r.json()

    # We fetch the two most recent data points from the API.
    # As this includes two latest value for our two humidity sensors.
    measurements = data
    humidity1 = measurements[0]['measure']['Humidity1']
    humidity2 = measurements[1]['measure']['Humidity2']
    return humidity1, humidity2


#########################################################
# TODO: complete the missing fields.
# AlternateID's from your device, sensor and capability.
deviceId ='xxx'
sensorAlternateId = 'xxx'
capabilityAlternateId = 'xxx'

# API endpoint to which we need to send our sensor data.
url = 'https://96e9f7bd-c38b-458d-8b98-630be0232fb8.eu10.cp.iot.sap/iot/gateway/rest/measures/' + deviceId
certificate = 'xxx' # e.g. certificate_name.pem

while True:

    # Retrieve sensor data from garden.
    humidity = getHumidity()
    print(humidity)

    # Upload sensor data to SAP IoT Service Cockpit.
    # TODO ...

    time.sleep(3) # Delay for 1 minute (60 seconds).
