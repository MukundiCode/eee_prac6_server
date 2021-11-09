from flask import Flask, send_file, render_template
import socket
import sys


app = Flask("name")

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/SensorStream')
def sensor_stream():
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt 
    return "sensor"

@app.route('/download')
def download_file():
    #TODO: Add code to download the file /data.sensorlog.txt
    return "download"

@app.route('/sendon')
def sendon():

    return "sendon"

@app.route('/sendoff')
def sendoff():
    return "sendoff"

@app.route('/status')
def status():
    return "status"

@app.route('/log')
def log():
    f = open("sensorlog.txt", "r+")
    for i in f :
        print(i)
    return "log"

@app.route('/exit')
def exit():
    return "exit"




#TODO Add the remaining functions requested either by adding more pages to the template or get fancy with more templates and better formatting




#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5080, debug=True) #Use this line to test basic functionality locally before trying to deploy on Pi
    #app.run(host='0.0.0.0', port=80)
