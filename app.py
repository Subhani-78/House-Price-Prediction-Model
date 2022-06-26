from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    return 'This app has been deployed on the cloud.'


if __name__ == "__main__":
    app.run(debug = True)


