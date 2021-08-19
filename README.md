# RasPiPostReqFlask

Getting a `POST` request to control an LED `off` & `on` state present on My [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)

:fire: :zap: My all Thanks goes to [Savvy](https://github.com/anomius) for guiding me thorugh the project :grinning:

## What Am I learning new?
- How to use Flask
- Raspi GPIO Control
- Usage of the `POST` request

## Usage

Go to `<serveripaddress>` to view the documentation

Go to `<serveripaddress>/on` to turn `ON` the LED

Go to `<serveripaddress>/off` to turn `OFF` the LED

[Turn ON](http://tally.ccnet.in/on)

[Turn OFF](http://tally.ccnet.in/off)


## Connection to GPIO

<img src="https://raw.githubusercontent.com/itsCharmander/RasPiPostReqFlask/master/static/project.png" alt="Schematic Diagram" width="350"/>

[Schematic Diagram](https://raw.githubusercontent.com/itsCharmander/RasPiPostReqFlask/master/static/project.png)

I have used a Resistor of `330KΩ` for Safety Reasons, In case the LED burns due to high current from the board it could result in some serious permanent damage to the board.

You can use it without resistor as well but make sure you are using a heavy LED for the same.

## Bibliography 

- [Official GPIO Documentation](https://www.raspberrypi.org/documentation/usage/gpio/)


- <img src="https://pi4j.com/1.2/images/j8header-3b-plus-large.png" alt="GPIO Diagram" width="350"/>

- [The Flask Project](https://flask.palletsprojects.com/en/2.0.x/)
