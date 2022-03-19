import os
from pdb import run
import time
import webbrowser
import pyautogui as py
import pyttsx3
import speech_recognition as sr
import subprocess

{
    'LinAlgText' : ["~/randy/Documents/Winter2022/Linear Algebra and Its Applications 5th Edition.pdf"]
}

def open_program(path_name):

    return subprocess.Popen(path_name)

def close_program(p):
    p.terminate()
    

# p=open_program("/usr/bin/caja --no-desktop --browser")
# time.sleep(3)
# print(p)
# close_program(p)


# # import speech_recognition as sr
# r = sr.Recognizer() # you recognize this line - initialize a Speech Recognizer object
# # mic represents your microphone
# mic = sr.Microphone()

# # this time, we'll use a mic instead of an audio recording. As far as Recognizer cares, mic is just a recording. 
# with mic as source: 
#   print("Recording...")
#   audio = r.listen(source)
#   print("Finished")

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

engine = pyttsx3.init()

def session():
    work = py.prompt(text='What do you need to work on? /n Enter URL or program executible command', title='Work' , default='https://byui.instructure.com/calendar#view_name=month&view_start=2022-03-19')
    if work[:5] != 'https':
        runprogram = True
    else:
        runprogram = False
    # get from user how long they want until reminded to return to work
    minutes = py.prompt(text='How long do you need a break for? (minutes)', title='Time?' , default='15')
    print(int(float(minutes)*60))

    # find out what to load when time is up
    breaktype = py.confirm(text='What are you taking a break on?', title='', buttons=['Browser', 'Program'])
    print(breaktype)

    time.sleep(int(float(minutes)*60))
    engine.say('Get ... to Work!')
    engine.runAndWait()
    if breaktype == 'Browser':
        py.hotkey('ctrl', 'w')
        if runprogram:
            open_program(work)
        else:
            webbrowser.open_new_tab(work)
    else:
        py.hotkey('ctrl', 'q')
        if runprogram:
            open_program(work)
        else:
            webbrowser.open_new(work)
            

numsessions = py.prompt(text='How many work sessions do you need?', title='Sessions?' , default='1')
lensession = py.prompt(text='How long do you want each of your work sessions to be? (minutes)', title='Length?' , default='25')
startbreak = py.confirm(text='Start with a break?', title='Start', buttons=['Yes', 'NO'])

if startbreak == 'Yes':
    print("Starting with break")
    session()
for i in range(int(numsessions)):
    print("Starting work session ")
    time.sleep(int(60*float(lensession)))
    session()