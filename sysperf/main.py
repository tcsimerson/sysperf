from flask import Flask, render_template
app = Flask(__name__)

# Setting configuration values for the Flask environment
sysperfVersion="1.0.0"

@app.route('/sysperf')
def index():
    return 'sysperf working'
app.add_url_rule('/','sysperf',index)


if __name__ == '__main__':
   app.run()
