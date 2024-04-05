from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
import os


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


@app.route('/message', methods=['POST', 'GET'])
def messageus():
    if request.method == 'POST':
        message = request.form.get('messageus')
        print(message)
    return redirect('/')

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
    app.run(debug=False)
