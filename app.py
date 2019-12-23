from flask import Flask, render_template, request, session, flash
from flask import url_for
import pandas as pd

rauan_url = Flask(__name__,
           template_folder="templates")


@rauan_url.route('/cv')
def download_cv():
    return url_for('static',filename='Rauan_Akylzhanov_CV.pdf')
@rauan_url.route('/about')
def about():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("about.html")


@rauan_url.route("/")
def home():
    return render_template("home.html")
@rauan_url.route("/jane")
def jane():
    return render_template("jane.html")
@rauan_url.route('/login', methods=['POST'])
def do_admin_login(page="about.html"):
    if request.form['password'] == 'password' and request.form['username'] =='username':
        session['logged_in'] = True
        return render_template(page)
    else:
        flash('wrong password!')
        return home()

if __name__ == "__main__":
    rauan_url.secret_key = b'|\xc8;M\x1a\xeb\nF\x1cQ\x86\xc4Q\xd4KG'
    rauan_url.run(debug=True)
