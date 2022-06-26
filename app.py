from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    logging.info("Testing Logging Module")
    return 'This app has been deployed on the cloud.'


if __name__ == "__main__":
    app.run(debug = True)


