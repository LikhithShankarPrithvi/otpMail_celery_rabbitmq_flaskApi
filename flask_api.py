from flask import Flask
from tasks import make_celery
from mail import send_otp_mail
from otp_gen import otp

app=Flask(__name__)
app.config['CELERY_BROKER_URL']='pyamqp://'
app.config['CELERY_RESULT_BACKEND']='rpc://'

celery=make_celery(app)

@app.route('/<name>')
def hello(name):
    reverse.delay(name)
    return(name)

@app.route('/send/<username>',methods=['GET'])
def send_mail(username):
    otp_mail_gen.delay(username,otp())
    #send_otp_mail(username,otp())
    return("An email containing 4-digit OTP is sent successfully")

@celery.task(name='flask_api.reverse')
def reverse(string):
    return string[::-1]

@celery.task(name='flask_api.otp_mail_gen')
def otp_mail_gen(username,number):
    send_otp_mail(username,number)
    return number

if(__name__ == '__main__'):
    app.run(debug=True)