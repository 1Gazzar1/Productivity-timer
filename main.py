import time 
from json import load

def get_mins_from_user(promt):
    
    while True : 
        inp = input(promt)
        if not inp.isnumeric():
           print("Invalid input")
        else : break
    return(float(inp)*60) 

def count_down(secs:int,sentence = ""):
    while secs : 
        print(secs)
        time.sleep(1)
        secs -= 1 
    print(sentence)

def show_time_in_nice_form(time_in_secs):
    secs = time_in_secs % 60
    mins = time_in_secs//60

    return f"{mins}:{secs}"

def Counter(time_needed_secs,sentence):
    start_time = time.time()
    while(True):
        Current_time = time.time()
        passed_time = int(Current_time - start_time)
        
        print(f"{sentence} {show_time_in_nice_form(int(passed_time))}")
        time.sleep(1)
        if time_needed_secs <= passed_time :
            break

def check_for_prefered_settings(promt):
    while True : 
        load()
        inp = input("do you want your prefered settings or not ?")
        


while True : 
    productivity_secs =  get_mins_from_user("How many mins do you want for the productivity timer ? : ")
    break_secs = get_mins_from_user("How many mins do you want for the break timer ? : ")
     
    count_down(3,"GO!!")

    Counter(productivity_secs,"Productivity Timer") 

    print("Break time :)")
    count_down(3,"Have Fun!!")

    Counter(break_secs,"Break Timer") 


