#import modules
import smtplib
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
import time

# setup gpio pins
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

# Print message on screen
print("Activate to proceed")
time.sleep(25)

# start loop
loop = "1"
while loop == "1":

    # test GPIO for input
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
