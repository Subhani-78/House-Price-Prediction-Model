from flask import Flask
import sys
from housing.logger import logging
from housing.exception import CodeException


app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    try:
        raise Exception("We are testing custom exception.")
    except Exception as e:
        housing = CodeException(e,sys)
        logging.info(housing.error_message)
        logging.info("Testing Logging Module")

    return 'This app has been deployed on the cloud.'


if __name__ == "__main__":
    app.run(debug = True)


