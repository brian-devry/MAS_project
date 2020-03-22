#import modules
import smtplib
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
import time

# setup gpio pins
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
# using pin 17 for input (for one input)
GPIO.setup(17, GPIO.IN)

# Print message on screen
print("Activate to proceed")
time.sleep(25)

# start loop
loop = "1"
while loop == "1":

    # test GPIO for input on pin 17
    if not GPIO.input(17):
        time.sleep(4)
    if not GPIO.input(17):

        # create email
        message = """Smoke Detector Activation"""
        msg = MIMEText(message)
        msg['subject'] = 'My Address'
        msg['from'] = 'myemail@gmail.com'
        msg['to'] = 'myverizonphone#@vtext.com'

        # send mail
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('myemail@gmail.com', 'myemailpassword')
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit
print("Message sent")
time.sleep(60)
while not GPIO.input(17):
    pass

# Function to run when motion detected
PIN_LED = 24
counter = 0
def detectMotionSensor(channel):
    GPIO.output(PIN_LED, GPIO.LOW)
    if GPIO.input(17):     # True = Rising
        global counter
        counter += 1
        times = datetime.datetime.now()
        GPIO.output(PIN_LED, GPIO.HIGH)
        print("Motion Detected: " + str(counter))
        print("Time: " + str(times))
