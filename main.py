from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/<domain>')
def hello(domain):
    try:
        return subprocess.check_output(["python", "DNSWhy/main.py" ,domain]).decode('ascii')
    except Exception as e:
        return "Error. Check domain!"


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


if __name__== "__main__":
    app.run()
