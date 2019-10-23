from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import urllib.request
import json
import pickle


"""create and configures an instance of a flask app"""
app = Flask(__name__)

encoder = pickle.load(open('encoder.pkl','rb'))

model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['GET', 'POST'])
def root():
    message = 'welcome home'
    return render_template('base.html', message=message)

@app.route('/request')
def request_data():
    data = request.get_json()
    accomodates = data.accomodates
    bathrooms = data.bathrooms
    bedrooms = data.bedrooms
    beds = data.beds
    bed_type = data.bed_type
    instant_bookable = data.instant_bookable
    minimum_nights = data.minimum_nights
    neighborhood = data.neighborhood
    room_type = data.room_type
    wifi = data.wifi
    security_deposit = 0
    cleaning_fee = 10
    features= {'accomodates':accomodates,'bathrooms':bathrooms, 'bedrooms':bedrooms,
                'beds': beds, 'bed_type':bed_type, 'instant_bookable':instant_bookable,
                'minimum_nights':minimum_nights, 'neighborhood':neighborhood,
                'room_type':room_type,'wifi':wifi, 'security_deposit':security_deposit,
                'cleaning_fee':cleaning_fee}
    predict_data= pd.DataFrame.from_dict(features)


# Above lies the dummy data.

if __name__ == '__main__':
    app.run(debug=True)
