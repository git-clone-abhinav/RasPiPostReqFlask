from flask import Flask
from flask import request
app = Flask(__name__)
# import led
import RPi.GPIO as GPIO
import markdown
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

@app.route("/")
def index():
    """Some Documentation"""

    # Open the ReadMe File
    #with open(os.path.dirname(app.root_path) + '/README.md', 'r' ) as markdown_file:
    with open('/home/pi/Desktop/RasPiPostReqFlask/README.md', 'r' ) as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)

@app.route("/on")
def on():
    GPIO.output(4, True)
    return "LED ON"


@app.route("/off")
def off():
    GPIO.output(4, False)
    return "LED OFF"

@app.route('/api/rgb', methods=['GET'])
def api_rgb():
    if 'rgb' in request.args:
        id = int(request.args['rgb'])
        print(id)
    else:
        return "Error: No id field provided. Please specify an rgb."

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 80, debug = True)
