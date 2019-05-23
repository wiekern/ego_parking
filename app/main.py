from flask import Flask, render_template
import osmapi
import requests
import random


app = Flask(__name__)

rest_server = "https://ego-vehicle-api.azurewebsites.net/api/v1"
api_key = "7443363c-4304-4c56-9df0-6af4af40c613"


msg_type = ['/vehicle/signals']

def get_request(url='', params=None):
    headers = {
        "X-Api-Key": api_key,
        'accept': 'application/json',
    }
    # params_data = str(urllib.parse.urlencode(params))
    URL = rest_server + url
    # print(URL)
    response = requests.get(URL, headers=headers)

    # print(response.text)
    return response.json()


@app.route("/")
def index():
    locations = []
    # get the location of one car via api key
    vehicle_state = get_request(url=msg_type[0])    
    car_loc = tuple(map(float, vehicle_state['location'].strip().split(',')))
    locations.append(car_loc)
    
    # dummy locations of cars
    xs = random.sample(range(40, 60), 10)
    ys = random.sample(range(0, 10), 10)
    locations += list(zip(xs, ys))
    # print(locations)

    return render_template('index.html', locations=locations)




    

if __name__ == '__main__':

    app.run()
    

    # api = osmapi.OsmApi()
    # print(api.NodeGet(123))
