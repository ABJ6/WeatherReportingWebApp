from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)

def get_weather_data(city):
    OPEN_WEATHER_MAP_URL = "http://api.openweathermap.org/data/2.5/weather"
    OPEN_WEATHER_MAP_API_KEY = "9d3d0c85b8c223e0c3aebba217e92c28"

    params = {
        'q': city,
        'appid': OPEN_WEATHER_MAP_API_KEY,
        'units': 'metric'
    }

    response = requests.get(OPEN_WEATHER_MAP_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        return None



@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City not provided'}), 400

    weather_data = get_weather_data(city)
    if not weather_data:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

    return jsonify(weather_data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
