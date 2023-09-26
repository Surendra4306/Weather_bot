from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("front_end.html")

@app.route("/get_weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    weather_info = fetch_weather(city)
    return jsonify({"weather_info": weather_info})

def fetch_weather(city):
    api_key = "Your_API_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return f"The weather in {city} is {temperature}°C and {weather_description}."
    else:
        return "Error fetching weather data."

if __name__ == "__main__":
    app.run(debug=True)
