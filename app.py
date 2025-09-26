from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "YOUR_OPENWEATHERMAP_KEY"

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(debug=True)
