import RPi.GPIO as GPIO
import time

on = True
off = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


#morse code alphabet: 1 unit for dot, 3 units for dash
alphabet = {'a':(1,3),'b':(3,1,1,1),'c':(3,1,3,1),'d':(3,1,1),'e':(0,1),'f':(1,1,3,1),'g':(3,3,1),'h':(1,1,1,1),'i':(1,1),'j':(1,3,3,3),'k':(3,1,3),'l':(1,3,1,1),'m':(3,3),'n':(3,1),'o':(3,3,3),'p':(1,3,3,1),'q':(3,3,1,3),'r':(1,3,1),'s':(1,1,1),'t':(0,3),'u':(1,1,3),'v':(1,1,1,3),'w':(1,3,3),'x':(3,1,1,3),'y':(3,1,3,3),'z':(3,3,1,1),'1':(1,3,3,3,3),'2':(1,1,3,3,3),'3':(1,1,1,3,3),'4':(1,1,1,1,3),'5':(1,1,1,1,1),'6':(3,1,1,1,1),'7':(3,3,1,1,1),'8':(3,3,3,1,1),'9':(3,3,3,3,1),'0':(3,3,3,3,3)}

#speed settings in seconds
slow = (.4)
normal = (.2)
fast = (.1)

speed = normal
message = input("Type in your message")

def textToMorse():
	#for each letter in the message
	for k in message.lower():
		#if the letter is in the morse code alphabet
		if k in alphabet:
			#for each number in the value of the letter key
			for n in alphabet[k]:
				GPIO.output(18, on)
				#assures the LED will remain on for the amount of time required (1 unit for dot, 3 units for dash)
				time.sleep(n * speed)
				GPIO.output(18,off)
				#creates a pause of 1 unit (dot) between parts of the same letter
				time.sleep(1 * speed)
		elif k == ' ':
			#if a space is used as in between words, it creates a pause of 7 units as it is standard in morse code
			time.sleep(7 * speed)


textToMorse()
GPIO.cleanup()			
