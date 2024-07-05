# WeatherAPI

A RESTful API that retrieves weather information for a specified city using the WeatherAPI.com API.

## Table of Contents

- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Technologies Used](#technologies-used)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/weather-api.git
```

2. Navigate to the project directory:

```bash
cd weather-api
```

3. Install the required dependencies:

```bash
pip install flask requests
```

4. Sign up for a free API key from WeatherAPI.com: https://www.weatherapi.com/signup.html

5. Replace the `api_key` variable in the `weather_api.py` file with your actual API key.

6. Run the API server:

```bash
python weather_api.py
```

The API server will start running on http://localhost:5000.

## API Documentation

### Endpoint: GET /weather

#### Description

Retrieves weather information for a specific city.

#### Request

- Method: GET
- URL: http://localhost:5000/weather
- Query Parameters:
  - city: Name of the city (required)

#### Response

- HTTP Status Code: 200 OK
- Body: JSON object containing weather information

```json
{
  "location": "City Name, State",
  "temperature": "Temperature in degrees Fahrenheit",
  "condition": "Weather condition (e.g., sunny, cloudy, rainy)",
  "wind_speed": "Wind speed in mph",
  "humidity": "Humidity percentage"
}
```

#### Error Responses

- HTTP Status Code: 404 Not Found
  - Body: JSON object with an error message

```json
{
  "error": "City not found"
}
```

## Technologies Used

- Python 3.x
- Flask framework
- requests library