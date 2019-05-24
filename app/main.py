from flask import Flask, render_template
import requests
import random
from counting_objects.core.main import main
import os


app = Flask(__name__)

rest_server = "https://ego-vehicle-api.azurewebsites.net/api/v1"
api_key = "7443363c-4304-4c56-9df0-6af4af40c613"
msg_type = ['/vehicle/signals']

def get_request(url='', params=None):
    headers = {
        "X-Api-Key": api_key,
        'accept': 'application/json',
    }
    URL = rest_server + url
    response = requests.get(URL, headers=headers)

    return response.json()


@app.route("/")
def index():
    locations = []
    # get the location of one car via api key
    vehicle_state = get_request(url=msg_type[0])    
    car_loc = tuple(map(float, vehicle_state['location'].strip().split(',')))
    locations.append(car_loc)
    
    # dummy locations of cars
    xs = random.sample(range(5, 35), 10)
    ys = random.sample(range(0, 15), 10)
    locations += list(zip(xs, ys))
    spot_xs = random.sample(range(5, 35), 10)
    spot_ys = random.sample(range(0, 15), 10) 
    spots = list(zip(spot_xs, spot_ys))

    return render_template('index.html', locations=locations, spots=spots)

@app.route("/getParkingSpots")
def getParkingSpots():
    main()
    parking_spots_imgs = os.listdir('/home/yyf/ego_parking/app/static/target_imgs')
    return render_template('parking-spots.html', parking_img=parking_spots_imgs)


if __name__ == '__main__':
    app.run()
    