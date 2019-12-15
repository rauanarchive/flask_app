from flask import Flask

rauan_url = Flask(__name__)

@rauan_url.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    rauan_url.run()
