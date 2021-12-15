from flask import Flask,render_template
app =  Flask(__name__)

@app.route ('/')
def index():
    users = ["Romeo","Alpha","November","Oscar"]
    return render_template('index.html', users = users)   

@app.route ('/user/<name>')
def user(name):
    return render_template('user.html', name=name)