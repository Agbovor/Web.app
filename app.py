from flask import Flask, render_template
from dotenv import load_dotenv
import os
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = str(os.getenv('MAIL_SERVER'))
app.config['MAIL_PORT'] = str(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def send():
    message = Message(
        subject= "Button Event",
        recipients = ["trumpalex108@gmail.com"],
        sender = "agbovoralex65@gmail.com"

    )

    message.body = "I pushed the button"

    try:
        mail.send(message)
        return "sent successfully"
    
    except Exception as e:
        return "sent failed"

# @app.route("/mail")
# def whereami():
#     return "<p>where are you indeed</p>"
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')