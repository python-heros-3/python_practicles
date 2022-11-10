import time 
from time import gmtime, strftime, localtime

def greet_me(time):

    if time > "24:00:00" and time < "12:00:00":
        return "hai sir ,Good Morning "
        
    if time > "12:00:00" and time < "16:00:00":
        return "hai sir Good afternoon"
    
    if time > "16:00:00" and time < "20:00:00":
        return "hai sir Good Evening"
    
    if time > "20:00:00" and time < "24:00:00":
        return "Have a good dreams sir, good night"


