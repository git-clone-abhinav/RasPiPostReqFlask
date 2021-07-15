from flask import Flask
app = Flask(__name__)
# import led
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

@app.route("/on")
def on():
    GPIO.output(4, True)
    return "LED ON"


@app.route("/off")
def off():
    GPIO.output(4, False)
    return "LED OFF"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 80, debug = True)
