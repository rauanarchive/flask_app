from flask import Flask, render_template

rauan_url = Flask(__name__,
           template_folder="templates")

@rauan_url.route('/')
def about():
    return render_template("about.html")


@rauan_url.route("/")
def home():
    return render_template("home.html")
    

if __name__ == "__main__":
    rauan_url.run(debug=True)
