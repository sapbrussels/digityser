from random import random
import requests # http://docs.python-requests.org/en/master/
import time


#Send random values (simulating a sensor) to the SAP cloud which can be retrieved by an app.
#Certificate Passphrase : TCBAUKkUf51Yhv6M


#Variables for connection

device_alt_id = '8a6d61e42f0847f6'
capability_alt_id = 'ee4d5f5a1eaf1d7b'
sensor_alt_id = '4580a048ef3995b4'


hostiot ='weather-station.eu10.cp.iot.sap/iot/gateway/rest/'
path = '/measures/'+device_alt_id
url = "https://"+hostiot+path






#Generate random values


#while(True):

temperature = round(random()*100)
humidity = random()*100
pressure = round(random()*2000)


print("\nValues to post: ", temperature, humidity, pressure)

payload = "{ \"capabilityAlternateId\": \""+capability_alt_id+"\",\"sensorAlternateId\": \""+sensor_alt_id+"\", \"measures\":" + str(temperature)+"}"

headers = {

        'content-type': "application/json",

        'cache-control': "no-cache"

        }



print("Payload to post: ", payload)



response = requests.request("POST", url, data=payload, headers=headers,cert=('./DigitYser-device_certificate.pem'))



print(response.status_code, response.text)

    #time.sleep(5)
