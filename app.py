from flask import Flask, render_template, request, session, flash
from flask import url_for
import pandas as pd

rauan_url = Flask(__name__,
           template_folder="templates")

import requests
from twilio.twiml.messaging_response import MessagingResponse


@rauan_url.route('/bot', methods=['POST','GET'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

@rauan_url.route('/cv')
def download_cv():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
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
