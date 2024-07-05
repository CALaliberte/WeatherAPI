#  RESTful API for Weather app using WeatherApi.com

from flask import Flask, request, jsonify

import requests

app = Flask(__name__)

api_key = "d7bf5ce80e8f4a40a4f122524240507"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        state = data["location"]["region"]
        temp = data["current"]["temp_f"]
        tempText = data["current"]["condition"]["text"]
        wind = data["current"]["wind_mph"]
        humidity = data["current"]["humidity"]
        return jsonify({
            'location': f'{location}, {state}',
            'temperature': f'{temp} degrees Fahrenheit',
            'condition': tempText,
            'wind_speed': f'{wind} mph',
            'humidity': f'{humidity}%'
        })
    elif response.status_code == 404:
        return jsonify({'error': 'City not found'}), response.status_code
    elif response.status_code == 401:
        return jsonify({'error': 'Invalid API key'}), response.status_code
    else:
        return jsonify({'error': 'Error fetching data'}), response.status_code
    
if __name__ == '__main__':
    app.run(debug=True)