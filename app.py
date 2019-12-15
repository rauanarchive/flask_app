from flask import Flask
rauan-url = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    rauan-url.run()
