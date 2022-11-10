import time
from time import gmtime, strftime, localtime
from greetings import greet_me
import wikipedia
import webbrowser
import pyttsx3

engine = pyttsx3.init('sapi5')

# print (webbrowser.open("who is president of America"))

print(f"Hai welcome, my name is alexa")
user_name = "jordan"

# # # accent_time = ['tim', 'time', 'tame']

while True:
    current_time = strftime ("%H:%M:%S", localtime() ) 
    speak = greet_me(current_time), " ", user_name
    print(greet_me(current_time), " ", user_name)
    engine.say(speak)
    engine.runAndWait()

    user = input("ask me anything:  ")
    
    if 'time'  in user:  # test1 passed for time detct
        print("Sir the time is : ", current_time)
        speak = "Sir the time is : ", current_time
        engine.say(speak)
        engine.runAndWait()

    
    # elif 'what' in user:  # query , search result doesnt wokrs proper, summary giving wrong, and somewytimes it doesnt trigger
    #     print("Sir, i dont know about this, but wikipedia says that : ")
    #     engine.say("Sir, i dont know about this, but wikipedia says that : ")
    #     engine.runAndWait()
    #     print( wikipedia.summary(user) [:100])
    #     speak = wikipedia.summary(user) [:100]
    #     engine.say(speak)
    #     engine.runAndWait()

    elif 'alexa' in user: # for searching whatever we typed
        engine.say("Opening Google for your answer")
        engine.runAndWait()
        webbrowser.open(f"https://www.google.com/search?q={user}")
    
    elif 'open youtube' in user: # simply opens the app for us
        engine.say("Opening youtube")
        engine.runAndWait()
        webbrowser.open(f"https://www.youtube.com")
 



