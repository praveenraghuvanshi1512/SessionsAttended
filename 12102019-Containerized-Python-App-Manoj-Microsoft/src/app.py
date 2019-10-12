from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    machine = socket.gethostname()
    return "Hello World from {machine}".format(machine=machine)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("5003"), debug=True)