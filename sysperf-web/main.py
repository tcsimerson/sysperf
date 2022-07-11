from flask import Flask, flash, render_template, request
from werkzeug.utils import secure_filename
import socket
import requests
import json
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/sysperf/"

# Setting configuration values for the Flask environment
sysperfVersion="1.0.0"
sarperfVersion="2.0.0"
flexperfVersion="4.0.0"

# Getting the container hostname
NODE_NAME=socket.gethostname()

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

@app.route('/flexperf/upload', methods = ['POST'] )
def fpUpload():
  # TBD:  make sysperf API calls to do the following:
  #     Get next project id (sysperf/getId)
  #     create the project data file (located in fcp-uploads
  #        
  #     unzip/tar-gunzip the files
  #     Check that there are enough sa data files to use
  #     Check/convert files to proper sysstat format
  #     Order the files in ascending data order
  #     Normalize the time interval
  #     Build time_template dictionary
  # Need to change eventually to something like this:
  # make API call to 

  # Building up the HTTP structure to be used by all API call
  baseUrl="http://sysperf:5000/sysperf/"
  header = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  # Seeing if a project file already exists
  query="email="+request.form['email']+"&customer="+request.form['customer']
  response=requests.get(baseUrl+"project/findByEmailCustomer?"+query, headers=header)
  if response.status_code == 404:
    # Getting the next project ID
    response=requests.get(baseUrl+"project/nextId", headers=header)
    projectId=response.json()

    # Build out json body
    projectData = {
      "id": projectId,
      "email": request.form['email'],
      "customer": request.form['customer']
    }
    # Post the data to create the file
    response=requests.post(baseUrl+"project/create", headers=header, data=json.dumps(projectData))

  # Building out the directory structure to store the uploaded files
  # TBD: leverage API to perform this task
  email=request.form["email"]
  customer=request.form["customer"]
  target_dir=app.config["UPLOAD_FOLDER"]+"fcp-uploads/"+email
  if not os.path.exists(target_dir):
    os.mkdir(target_dir)
  target_dir=target_dir+"/"+customer
  if not os.path.exists(target_dir):
    os.mkdir(target_dir)

  # Moving the uploaded files into the target directory
  files = request.files.getlist("file")
    for f in files:
      filename = secure_filename(f.filename)
      f.save(target_dir + "/" + filename )
  form_data = request.form

  # Validate files (Check for enough files, proper suffix, proper file type, etc)
  response=requests.get(baseUrl+"files/validate/"+projectId, headers=header)

  # Unzip/untar the uploaded files
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"files/extract/"+projectId, headers=header)

  # Convert data files to current sysstat format
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"files/convert/"+projectId, headers=header)

  # Render the template file with all the details
  return render_template('fcp-upload.html',version=flexperfVersion,nodename=NODE_NAME,result=form_data,filenames=files)

@app.route('/flexperf/process')
def fpProcess():
  # Do all sorts of processing related stuff.  Final Excel spreadsheet
  #   will be presented back.
  # for errors, use a template upload_error.html with the pertinent
  #   error codes and text.

  # TBD:  shortcircuit all of the processing if the project data already exists.
  # Just generate the output.
  #if all_data_exists:
  #  generate_output_process
  #  return render_template('fcp-process.html')

  # Create ordered list of files based upon date
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"data/orderByDate/"+projectId, headers=header)

  # Create time template (determine time interval, create time template)
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"data/timeTemplate/"+projectId, headers=header)

  # Collect information from system.txt data file
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"data/getSystem/"+projectId, headers=header)

  # Calculate the memory configuration if system.txt not present or did not have the memory configuration details
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #if ! skip_core_mem:
  #  response=requests.get(baseUrl+"data/memoryCalculate/"+projectId, headers=header)

  # Create template data hash to be stored
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"data/getSystem/"+projectId, headers=header)

  # Render the template file with all the details
  return render_template('fcp-process.html')

###############################################
# sar-perf related API/web pages
@app.route('/sar-perf')
def spIndex():
  return render_template('spw-index.html',version=sarperfVersion,nodename=NODE_NAME)

@app.route('/sar-perf/upload')
def spUpload():
  # Building up the HTTP structure to be used by all API call
  baseUrl="http://sysperf:5000/sysperf/"
  header = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  # Setting locally global variables
  email=request.form["email"]
  customer=request.form["customer"]

  # Seeing if a project file already exists
  query="email="+email+"&customer="+customer
  response=requests.get(baseUrl+"project/findByEmailCustomer?"+query, headers=header)
  if response.status_code == 404:
    # Getting the next project ID
    response=requests.get(baseUrl+"project/nextId", headers=header)
    projectId=response.json()

    # Build out json body
    projectData = {
      "id": projectId,
      "email": email,
      "customer": customer,
      "name": "sar-perf "+str(projectId),
      "type": "sar-perf"
    }
    # Post the data to create the file
    response=requests.post(baseUrl+"project/create", headers=header, data=json.dumps(projectData))

  # Building out the directory structure to store the uploaded files
  # TBD: leverage API to perform this task
  target_dir=app.config["UPLOAD_FOLDER"]+"fcp-uploads/"+email
  if not os.path.exists(target_dir):
    os.mkdir(target_dir)
  target_dir=target_dir+"/"+customer
  if not os.path.exists(target_dir):
    os.mkdir(target_dir)

  # Moving the uploaded files into the target directory
  files = request.files.getlist("file")
    for f in files:
      filename = secure_filename(f.filename)
      f.save(target_dir + "/" + filename )
  form_data = request.form

  # Validate files (Check for enough files, proper suffix, proper file type, etc)
  response=requests.get(baseUrl+"files/validate/"+projectId, headers=header)

  # Unzip/untar the uploaded files
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"files/extract/"+projectId, headers=header)

  # Convert data files to current sysstat format
  #query="email="+request.form['email']+"&customer="+request.form['customer']
  #response=requests.get(baseUrl+"files/convert/"+projectId, headers=header)

  # Render the template file with all the details
  return render_template('spw-upload.html',version=sarperfVersion,nodename=NODE_NAME,result=form_data,filenames=files)

@app.route('/sar-perf/process')
def spProcess():
  # Do all sorts of processing related stuff.  Final Excel spreadsheet
  #   will be presented back.
  # for errors, use a template upload_error.html with the pertinent
  #   error codes and text.
  return render_template('spw-process.html')

if __name__ == '__main__':
  app.run()
