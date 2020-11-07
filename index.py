from flask import Flask
import sys, serial, time


app = Flask(__name__)


portName = '/dev/ttyUSB0'
baudRate = 9600

relay_1_on = b"\x0E"
relay_2_on = b"\x0D"
all_relays_off = b"\x0F"

command_1=b"\x50"
command_2=b"\x51"

def initialization():

    ser = serial.Serial(portName,baudRate)
    ser.write(command_1)
    time.sleep(0.3)
    ser.write(command_2)
    ser.close()


initialization()

def relay(port):
    ser = serial.Serial(portName,baudRate)
    ser.write(port)
    time.sleep(0.5)
    ser.write(all_relays_off)
    ser.close()


@app.route('/1', methods=['POST'])
def relay1():
    relay(relay_1_on)
    return 'ok'


@app.route('/2', methods=['POST'])
def relay2():
    relay(relay_2_on)
    return 'ok'




