from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"  # Replace with your actual API key

@app.route('/', methods=['GET', 'POST'])
def index():
    conversion_result = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        target_currency = request.form['currency']
        url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and 'conversion_rates' in data:
            rate = data['conversion_rates'].get(target_currency)
            if rate:
                conversion_result = amount * rate
            else:
                conversion_result = "Invalid target currency."

    return render_template('index.html', result=conversion_result)

if __name__ == '__main__':
    app.run(debug=True)
