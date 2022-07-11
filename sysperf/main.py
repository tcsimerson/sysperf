from flask import Flask, request
import json
import os
app = Flask(__name__)

# Setting configuration values for the Flask environment
sysperfVersion="1.0.0"
dataDir="/sysperf/data"

@app.route('/sysperf')
def index():
  return 'sysperf working'
app.add_url_rule('/','sysperf',index)

##################################################################
# PROJECT section
# Getting next project ID from id.json and incrementing
# ID to next value
@app.route('/sysperf/project/nextId')
def spProjectNextId():
  # Get the current ID
  idFile = open(dataDir+"/id.json","r")
  idJson=json.load(idFile)
  returnId=idJson['currentId']
  idFile.close()

  # Increment the ID
  idJson['currentId'] += 1

  # write out the data file with new ID
  idFile = open(dataDir+"/id.json","w")
  json.dump(idJson,idFile,indent=2,sort_keys=True)
  idFile.close()

  # return the JSON with the current ID
  return str(returnId)

# Getting project data based upon provided project ID
# Returns 200 if found, or 404 if not found.
@app.route('/sysperf/project/<projectId>')
def spProjectGet(projectId):
  assert projectId == request.view_args['projectId']
  # Check to see if the project file exists
  if os.path.exists(dataDir+"/"+projectId):
    # TBD
    # Open the project file and return the JSON string
    return "found", 200
  else:
    return "not found", 404

# Getting project data using e-mail and customer name
# Returns 200 if found, or 404 if not found.
@app.route('/sysperf/project/findByEmailCustomer')
def spProjectGetByEmailCustomer():
  # Get parts of the query
  email=request.args.get('email')
  customer=request.args.get('customer')
  print("email="+email)
  print("customer="+customer)

  # Check to see if the project file exists
  if os.path.exists(dataDir+"/"+email+":"+customer):
    # TBD
    # Open the project file and return the JSON string
    return "found", 200
  else:
    return "not found", 404

# Creating a project JSON file from the provided
# JSON data
@app.route('/sysperf/project/create', methods=['POST'])
def spProjectCreate():
  # Getting JSON from post request
  projectJson=request.json

  # Open the project file
  fileName=projectJson['email']+":"+projectJson['customer']+".json"
  projectFile=open(dataDir+"/"+fileName,"w")
  json.dump(projectJson,projectFile,indent=2,sort_keys=True)
  projectFile.close()
  return "wrote data file successfully",200

##################################################################
# FILES section
# Getting project data based upon provided project ID
# Returns 200 if found, or 404 if not found.
@app.route('/sysperf/files/validate/<projectId>')
def spFilesValidate(projectId):
  assert projectId == request.view_args['projectId']

  # Check to see if the project file exists
  if os.path.exists(dataDir+"/"+projectId):
    # TBD
    # Open the project file and return the JSON string
    return "found", 200
  else:
    return "not found", 404

# Main call
if __name__ == '__main__':
   app.run()
