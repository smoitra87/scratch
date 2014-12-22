import os, sys
import random

audio = {
    'Calm Down' : 'cd.wav',
    'Genius!' : 'g.wav',
    'Nice Try!' : 'nt.wav',
    'One Tight' : 'ot.wav',
    'Which tree did you come down from?' : 'tr.wav',
    'Happy Birthday Pallavi' : 'wishes.wav'
}


while True:
    raw_input("What's up? ")
    k,v = random.choice(audio.items())
    print(k)
    os.system('aplay -q ' + v )


