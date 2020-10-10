from twython import Twython    
from primary_key import (API_key,API_secret_key,access_token_key,access_token_secret_key)
from quotes import tweet
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
GPIO.setmode(BCM)
GPIO.setwarnings(false)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
flag=false
count=0
while(true):
   ti=time.localtime(time.time())
   if(ti.tm_hour==4 && ti.tm_min<=5 && flag==false):
     GPIO.output(24,HIGH)
     twitter=Twython(API_key,API_secret_key,access_token_key,access_token_secret_key)
     try:
       twitter.update_status(status=tweet[count])
       print("Tweeted: %s" % random.choice(tweet[count]))
       flag=true;
       ++count
       if(count>=1000):
          count=0
     except:
       print("Please! Check your internet connection")
     finally:
 GPIO.output(24,LOW)
   else
     if(ti.tm_hour>=5):
       flag=false
     humid,temp=Adafruit_DHT.read_retry(11,6)
     if(temp<15):
       GPIO.output(14,LOW)
     else :
       GPIO.output(14,HIGH)

