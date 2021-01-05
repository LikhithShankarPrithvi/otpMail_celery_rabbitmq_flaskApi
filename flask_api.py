from flask import Flask
from mail import send_otp_mail
from otp_gen import otp

app=Flask(__name__)

@app.route('/')
def hello():
    return('Hello World')

@app.route('/send/<username>',methods=['GET'])
def send_mail(username):
    send_otp_mail(username,otp())
    return username

app.run(debug=True)