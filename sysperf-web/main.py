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

###############################################
# sar-perf related API/web pages
@app.route('/sar-perf')
def spIndex():
    return render_template('spw-index.html',version=sarperfVersion,nodename=NODE_NAME)

@app.route('/sar-perf/testapi')
def spTest():
    r=requests.get("http://sysperf:5000/sysperf")
    api_return=r.text
    return render_template('test.html',apiresult=api_return,nodename=NODE_NAME)

@app.route('/sar-perf/upload')
def spUpload():
    # Do all sorts of upload related stuff
    # for errors, use a template upload_error.html with the pertinent
    #   error codes and text.
    return render_template('spw-upload.html')

@app.route('/sar-perf/process')
def spProcess():
    # Do all sorts of processing related stuff.  Final Excel spreadsheet
    #   will be presented back.
    # for errors, use a template upload_error.html with the pertinent
    #   error codes and text.
    return render_template('spw-process.html')

###############################################
# flexperf relate API/web pages
@app.route('/flexperf')
def fpIndex():
    return render_template('fcp-index.html',version=flexperfVersion,nodename=NODE_NAME)

@app.route('/flexperf/testapi')
def fpTest():
    r=requests.get("http://sysperf:5000/sysperf")
    api_return=r.text
    return render_template('test.html',apiresult=api_return,nodename=NODE_NAME)

@app.route('/flexperf/upload')
def fpUpload():
    # Do all sorts of upload related stuff
    # for errors, use a template upload_error.html with the pertinent
    #   error codes and text.
    return render_template('fcp-upload.html')

@app.route('/flexperf/process')
def fpProcess():
    # Do all sorts of processing related stuff.  Final Excel spreadsheet
    #   will be presented back.
    # for errors, use a template upload_error.html with the pertinent
    #   error codes and text.
    return render_template('fcp-process.html')

if __name__ == '__main__':
   app.run()
