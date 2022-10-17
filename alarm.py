import time
from time import strftime
from playsound import playsound

current_time = strftime("%H:%M:%S", time.localtime())

print(f"Time right now is :{current_time}")

wake_up_time = input("What time do you want to wake up? : ")

while True :
  from time import gmtime, strftime

  current_time = strftime("%H:%M:%S", time.localtime())

  print(f"Time right now is :{current_time}")

  if wake_up_time == current_time:
    print("Time to wake up")
    playsound("justin_bieber-love_me.mp3")
    break