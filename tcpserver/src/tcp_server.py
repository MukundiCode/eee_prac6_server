import socket
import sys
import threading
from flask import Flask, render_template

f = open("/data/sensorlog.txt", "w+")
sensorLogData = []

#establishing connection
global conn
conn = None
TCP_IP = '0.0.0.0'
TCP_PORT = 5003
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
newconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newconnection.bind((TCP_IP, TCP_PORT))
newconnection.listen(1)
conn, addr = newconnection.accept()


#method for handling data reception
def getData(newconnection):
    #conn, addr = newconnection.accept()
    print('Connection address:', addr)
    with newconnection:
        while True:
            data = conn.recv(1024).decode()
            arr = data.split(" ")
            #print(arr[0])
            if(arr[0] == "Sending"):
                statusResponse(data)
            sensorLogData.append(data)
            print('\nReceived', data)
            f.write("\nReceived: ")
            f.write(data)
            f.flush()
            if not data: break


#interface stuff
app = Flask(__name__)

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
    print("sendon")
    data = "sendon"
    conn.send(data.encode())
    return index()

@app.route('/sendoff')
def sendoff():
    print("sendoff")
    data = "sendoff"
    conn.send(data.encode())
    return index()

@app.route('/status')
def status():
    print("status")
    data = "status"
    conn.send(data.encode())
    return index()

@app.route('/statusResponse')
def statusResponse(response):
    return response

@app.route('/log')
def log():
    f = open("/data/sensorlog.txt", "w+")
    response = ""
    for i in range(len(sensorLogData)-1,0, -1):
        response = response + sensorLogData[i] + " \n"
    for i in f :
        print(i)
    return response

@app.route('/exit')
def exit():
    return "exited"

if __name__ == '__main__':
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)).start()
    getData(newconnection=newconnection)