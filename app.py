from flask import Flask
import os
from flask_mail import Mail, Message
app = Flask(__name__)
mail= Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mymail@gmail.com'
app.config['MAIL_PASSWORD'] = 'mypass'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/bomb/<string:t>/<string:s>/<string:m>")
def bomb(t,s,m): 
    msg = Message(s, sender = 'mymail@gmail.com', recipients = [t])
    msg.body = m
    mail.send(msg)
    return "Sent"


if __name__ == '__main__': 
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
