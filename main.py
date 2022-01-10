from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/<domain>')
def hello(domain):
    try:
        return subprocess.check_output(["python", "DNSWhy/main.py" ,domain]).decode('ascii')
    except Exception as e:
        return "Error. Check domain!"

if __name__== "__main__":
    app.run()
