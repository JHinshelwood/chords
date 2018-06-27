import random
import os
import sys, signal

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

notes = ["C", "Db", "D", "Eb", "E", "F", "F#", "Gb", "G", "Ab", "A", "Bb", "B"]
chords = ["maj7", "min7", "7", "min7b5"]
prev = []

def genr(size):
    num = random.randrange(0, size)
    return num

def getNote():
    return notes[genr(len(notes))]

def printNote():
    print(getNote())

def getChord():
    return chords[genr(len(chords))]

def gen():
    return getNote() + getChord()

def checkPrev(c):
    if c in prev:
        return False
    return True

def playAudio(fullC):
    fileString = "aplay " + fullC + ".wav"
    os.system(fileString)


input("Press enter to generate a new chord...")

    
while(True):
    
    c = gen()

    while not checkPrev(c):
        c = gen()

    if (len(prev) > 5):
        del prev[0]

    
    prev.append(c)
    print(c) 
    playAudio(c)
    
   
