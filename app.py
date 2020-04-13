"""
    __author__ = Johana Luna, Stefano Ruiz
    __credits__ = Justin Hsieh
    __license__ = MIT License
    __version__ = 1.1
"""

from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

"""create and configures an instance of a flask app"""
app = Flask(__name__)

encoder = pickle.load(open('encoder.pkl', 'rb'))

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def root():
    """Root site directory for the app.Renders only the base.html template.
       :return: render_template
    """
    message = 'welcome home'
    return render_template('base.html', message=message)


@app.route('/request')
def request_data():
    """Gets data in JSON format and runs it through the model.
       :return: JSON file.
    """
    # Non-default values. Needs to have user input or breaks the app.
    # TODO Accomodate has a spelling error. Needs to be changed to "accommodate".
    accomodates = [int(request.args.get('accomodates'))]
    bathrooms = [float(request.args.get('bathrooms'))]
    bedrooms = [float(request.args.get('bedrooms'))]
    beds = [float(request.args.get('beds'))]
    bed_type = [int(request.args.get('bed_type'))]
    instant_bookable = [int(request.args.get('instant_bookable'))]
    minimum_nights = [int(request.args.get('minimum_nights'))]
    neighborhood = [int(request.args.get('neighborhood'))]
    room_type = [int(request.args.get('room_type'))]
    wifi = [int(request.args.get('wifi'))]

    # Defaulted values
    security_deposit = 0
    cleaning_fee = 10

    features = {'accomodates': accomodates, 'bathrooms': bathrooms, 'bedrooms': bedrooms,
                'beds': beds, 'bed_type': bed_type, 'instant_bookable': instant_bookable,
                'minimum_nights': minimum_nights, 'neighborhood': neighborhood,
                'room_type': room_type, 'wifi': wifi, 'security_deposit': security_deposit,
                'cleaning_fee': cleaning_fee}

    # Converts the data into a DataFrame object.
    predict_data = pd.DataFrame(features, index=[1])
    features_encoder = encoder.transform(predict_data)

    # Feeds the data into the model.
    prediction = model.predict(features_encoder)

    # Returns prediction in a JSON format and within, a float.
    res =  [format(prediction[0], '.2f'),features]
    return (render_template('predictor.html', res=res))


if __name__ == '__main__':
    app.run(debug=True)
