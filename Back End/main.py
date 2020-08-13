from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

MOTION = {'IN1': 1, 'IN2': 2}
LED = {'FLED': 3, 'RLED': 4}
PUMP = {'PUMP1': 5, 'PUMP2': 6}
CAM = {'IN1': 7, 'IN2': 8}
SPEED = 9

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(MOTION['IN1'], GPIO.OUT)
GPIO.setup(MOTION['IN2'], GPIO.OUT)
GPIO.setup(LED['FLED'], GPIO.OUT)
GPIO.setup(LED['RLED'], GPIO.OUT)
GPIO.setup(PUMP['PUMP1'], GPIO.OUT)
GPIO.setup(PUMP['PUMP2'], GPIO.OUT)
GPIO.setup(CAM['IN1'], GPIO.OUT)
GPIO.setup(CAM['IN2'], GPIO.OUT)
GPIO.setup(SPEED, GPIO.OUT)
SPD = GPIO.PWM(SPEED, 140000)

SPD.start(0)

spd_temp = 0

@app.route('/', methods=['GET'])
def led():
	status = request.args.get('status')
	speed = request.args.get('speed')

	SPD.ChangeDutyCycle(int(speed))
	if spd_temp == 0 or spd_temp != speed:
		spd_temp = speed
		return jsonify({'message': 'Speed ' + speed})

	if status == 'Pump1_OFF':
		GPIO.output(PUMP['PUMP1'], GPIO.LOW)
		return jsonify({'message': 'Pump 1 Turned OFF'})

	elif status == 'Pump1_ON':
		GPIO.output(PUMP['PUMP1'], GPIO.HIGH)
		return jsonify({'message': 'Pump 1 Turned ON'})

	elif status == 'Pump2_OFF':
		GPIO.output(PUMP['PUMP2'], GPIO.LOW)
		return jsonify({'message': 'Pump 2 Turned OFF'})

	elif status == 'Pump2_ON':
		GPIO.output(PUMP['PUMP2'], GPIO.HIGH)
		return jsonify({'message': 'Pump 2 Turned ON'})

	elif status == 'FLED_OFF':
		GPIO.output(LED['FLED'], GPIO.LOW)
		return jsonify({'message': 'Front LED Turned OFF'})

	elif status == 'FLED_ON':
		GPIO.output(LED['FLED'], GPIO.HIGH)
		return jsonify({'message': 'Front LED Turned ON'})

	elif status == 'RLED_OFF':
		GPIO.output(LED['RLED'], GPIO.LOW)
		return jsonify({'message': 'Rear LED Turned OFF'})

	elif status == 'RLED_ON':
		GPIO.output(LED['RLED'], GPIO.HIGH)
		return jsonify({'message': 'Rear LED Turned ON'})

	elif status == 'front':
		GPIO.output(MOTION['IN1'], GPIO.LOW)
		GPIO.output(MOTION['IN2'], GPIO.HIGH)
		return jsonify({'message': 'Bot Moving in forward direction', 'Speed' : speed})

	elif status == 'back':
		GPIO.output(MOTION['IN1'], GPIO.HIGH)
		GPIO.output(MOTION['IN2'], GPIO.LOW)
		return jsonify({'message': 'Bot Moving in backward direction', 'Speed': speed})

	elif status == 'right':
		GPIO.output(MOTION['IN1'], GPIO.HIGH)
		GPIO.output(MOTION['IN2'], GPIO.HIGH)
		return jsonify({'message': 'Bot Moving in right direction', 'Speed': speed})

	elif status == 'left':
		GPIO.output(MOTION['IN1'], GPIO.LOW)
		GPIO.output(MOTION['IN2'], GPIO.LOW)
		return jsonify({'message': 'Bot Moving in left direction', 'Speed': speed})

	elif status == 'stop':
		return jsonify({'message': 'Bot Stopped'})

	elif status == 'cam_left':
		GPIO.output(CAM['IN1'], GPIO.LOW)
		GPIO.output(CAM['IN2'], GPIO.HIGH)
		return jsonify({'message': 'Camera turning left'})

	elif status == 'cam_right':
		GPIO.output(CAM['IN1'], GPIO.HIGH)
		GPIO.output(CAM['IN2'], GPIO.LOW)
		return jsonify({'message': 'Camera turning right'})
		
	else:
		return jsonify({'message': 'Invalid Input'})
