from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    greeting = os.getenv('GREETING', 'سلام از پایتون PaKiani!')
    return f"<h1>{greeting}</h1><p>این یک اپ ساده Flask هست!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)