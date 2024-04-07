from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
from twilio.rest import Client
from dotenv import load_dotenv 
import os

load_dotenv()
twilio_key = os.getenv('TWILIO_KEY')
twilio_sid = os.getenv('TWILIO_SID')
print(twilio_key,twilio_sid,sep=' ')
account_sid = twilio_sid 
auth_token = twilio_key 
client = Client(account_sid, auth_token)

def send_message(message_text):
    try:
        client.messages.create(
        from_='+12567276832',
        body = message_text,
        to='+2330257330594'
        )
    except:
        pass

  

app = Flask(__name__)
app.config["UPLOAD_DIRECTORY"] = 'static/images'
app.config["MAX_CONTENT_LENGHT"] = 20*1024*1024
app.config["ALLOWED_EXTENTIONS"] = ['.jpg', '.png', '.jpeg', '.gif']

# For placing Home page images


@app.route("/", methods=['POST', 'GET'])
def hompage():
    logo = os.path.join(app.config["UPLOAD_DIRECTORY"], 'LOGO.png')
    chatbot = os.path.join(app.config["UPLOAD_DIRECTORY"], 'aibot.jpg')
    aiteach= os.path.join(app.config["UPLOAD_DIRECTORY"], 'aiteach.png')
    comvision = os.path.join(app.config["UPLOAD_DIRECTORY"], 'comvision.jpg')
    nice = os.path.join(app.config["UPLOAD_DIRECTORY"], 'solu.png')
    vision2 = os.path.join(app.config["UPLOAD_DIRECTORY"], 'airev.png')
    autoai = os.path.join(app.config["UPLOAD_DIRECTORY"], 'aiauto.png')
    vision = os.path.join(app.config["UPLOAD_DIRECTORY"], 'yolo.jpeg')
    vision1 = os.path.join(app.config["UPLOAD_DIRECTORY"], 'ai.png')
    freelance =  os.path.join(app.config["UPLOAD_DIRECTORY"], 'freelancing.jpeg')
    robotics =  os.path.join(app.config["UPLOAD_DIRECTORY"], 'robotics.png')
    consulting =  os.path.join(app.config["UPLOAD_DIRECTORY"], 'consult.jpg')
    return render_template('index.html', logo=logo, chatbot=chatbot,
                           aiteach=aiteach, nice=nice,
                           comvision = comvision,
                           vision2=vision2, autoai=autoai,
                           vision=vision, vision1=vision1,
                           freelance = freelance,
                           robotics = robotics,
                           consulting=consulting
                           )

# For receiving messages from user


@app.route('/submit', methods=['POST', 'GET'])
def messageus():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        country = request.form.get('country')
        text = request.form.get('serviceDescription')
        data = {
            'name':first_name+' '+last_name,
            'email':email,
            'country':country,
            'message':text
        }
        send_message(message_text=data)
        
    return redirect('/bookus')

@app.route('/bookus',methods=['POST', 'GET'])
def bookus():
    logo = os.path.join(app.config["UPLOAD_DIRECTORY"], 'LOGO.png')
    return render_template('bookus.html',logo=logo)

@app.route('/pricing',methods=['POST', 'GET'])
def pricing():
    logo = os.path.join(app.config["UPLOAD_DIRECTORY"], 'LOGO.png')
    return render_template('pricing.html',logo = logo)

@app.route('/courses',methods=['POST', 'GET'])
def courses():
    logo = os.path.join(app.config["UPLOAD_DIRECTORY"], 'LOGO.png')
    return render_template('courses.html',logo = logo)


if __name__ == '__main__':
    app.run(debug=True)
