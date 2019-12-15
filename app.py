from flask import Flask

rauan_url = Flask(__name__)

@rauan_url.route("/")
def hello():
    lines = [
            "My name is Rauan Akylzhanov",
            "I created this website to train my skills"
            ]
    return "\n".join(lines)
    

if __name__ == "__main__":
    rauan_url.run()
