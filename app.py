# from flask import Flask, render_template
# from dotenv import load_dotenv
# import os
# from flask_mail import Mail, Message

# load_dotenv()

# app = Flask(__name__)

# app.config['MAIL_SERVER'] = str(os.getenv('MAIL_SERVER'))
# app.config['MAIL_PORT'] = s(os.getenv('MAIL_PORT'))
# app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
# app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

# mail = Mail(app)

# @app.get('/')
# @app.post('/')
# def sendmail():
#     if request.metod == "POST":

#         fullname = request.form.get("name")
#         senderemail = request.form.get("email")
#         # recieveremail = request.form.get("remail")
#         messagebody = request.form.get("message")

#         message = Message(
#             subject= fullname,
#             recipients = [senderemail],
#             sender = "agbovoralex65@gmail.com"

#     )

#     message.body = messagebody

#     try:
#         mail.send(message)
#         return render_template('thankyou.html')
    
#     except Exception:
#         e = Exception
#         print(e)

# # @app.route("/mail")
# # def whereami():
# #     return "<p>where are you indeed</p>"

# if request.method == 'GET':
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug = True, host = '0.0.0.0')

from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def sendmail():
    if request.method == "POST":
        fullname = request.form.get("name")
        senderemail = request.form.get("semail")
        recieveremail = request.form.get("remail")
        messagebody = request.form.get("txtarea")

        message = Message(
            subject="Button Event",
            recipients=["trumpalex108@gmail.com"],
            sender="agbovoralex65@gmail.com"
        )

        message.body = messagebody

        try:
            mail.send(message)
            return render_template('thankyou.html')
        except Exception as e:
            print(e)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
