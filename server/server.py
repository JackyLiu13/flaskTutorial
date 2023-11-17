from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials= True)

@app.route("/")
def home():
    return {"Hello":"World"}


@app.route("/members")
def members():
    return {"Members":["m1","m2","m3"]}

if __name__ == "__main__":
    app.run(debug=True)