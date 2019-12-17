from flask import Flask, render_template, request, session

rauan_url = Flask(__name__,
           template_folder="templates")

@rauan_url.route('/about')
def about():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("about.html")


@rauan_url.route("/")
def home():
    return render_template("home.html")

@rauan_url.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
        return home()

if __name__ == "__main__":
    rauan_url.run(debug=True)
