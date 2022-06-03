from flask import Flask, render_template
import socket
import requests
app = Flask(__name__)

# Setting configuration values for the Flask environment
sysperfVersion="1.0.0"
sarperfVersion="2.0.0"
flexperfVersion="4.0.0"

# Getting the container hostname
NODE_NAME=socket.gethostname()

@app.route('/sar-perf')
def spIndex():
    return render_template('index.html',version=sarperfVersion,nodename=NODE_NAME)

@app.route('/sar-perf/testapi')
def spText():
    r=requests.get("http://sysperf:5000/sysperf")
    api_return=r.text
    return render_template('test.html',apiresult=api_return,nodename=NODE_NAME)

@app.route('/sar-perf/upload')
def spUpload():
    # Do all sorts of upload related stuff
    # for errors, use a template upload_error.html with the pertinent
    #   error codes and text.
    return render_template('upload.html')

if __name__ == '__main__':
   app.run()
