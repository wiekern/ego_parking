# Ego Artificial Parking
A promising project of helping drivers to park the car. Via the hot technology of deep learning provides a optimal solution to avoid mutiple drivers drive for less parking slots, improving the efficiency of usage of parking places.

## Usage

1. Install all dependencies
  `pip install -r requirements.txt`
  
2. Execute `python main.py` under folder 'app/'

3. Visit http://localhost:5000/


## Deep Learning Model
To run the AI model, please download pre-trained model file from https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5, then putting it under the folder 'app/static/', then jump back to the step *Usage* to run the server, now you are available to visit http://localhost:5000/getParkingSpots 

This part aims to have the real-time scenario of a parking spot, meanwhile, the data about the usage of the parking spot is stored. As a result, we are able to reccomend free parking places to drivers instantly, what's more, by analyzing the data in the past we can predict how likely a parking spot will be fully taken.
