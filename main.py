import time 
import json
import winsound

def load_prefrences():
    with open("details.json") as file :
        data = json.load(file)
    return data

def save_prefrences(prefrences):

    with open("details.json","w") as file:
        json.dump(
            prefrences,file
        )

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

def check_for_prefered_settings(promt) -> bool:
    while True :
        data = load_prefrences()   
        print(f'your saved prefrences are {data["fav_work_time"]} for work mins and {data["fav_rest_time"]} for rest mins')
        inp = input(promt)
        
        if inp == "y" : 
            return True
        elif inp == "n" : 
            return False
        else : 
            print("Invalid input")

def alert():
    for _ in range(3) : 
        winsound.Beep(1000,500)
        time.sleep(1)

data = load_prefrences()        

while True : 
    if check_for_prefered_settings("do you want your prefered settings or not ?(y/n)") : 
        productivity_secs , break_secs = data["fav_work_time"]*60,data["fav_rest_time"]*60
    else : 
        productivity_secs =  get_mins_from_user("How many mins do you want for the productivity timer ? : ")
        break_secs = get_mins_from_user("How many mins do you want for the break timer ? : ")
    
    save_prefrences(
                    {
                    "fav_work_time" : productivity_secs//60
                    ,"fav_rest_time" : break_secs//60
                    })
    count_down(3,"GO!!")

    Counter(productivity_secs,"Productivity Timer") 

    print("Break time :)")
    alert()
    input("press enter to continue")
    count_down(3,"Have Fun!!")

    Counter(break_secs,"Break Timer") 

    print("Break time is Over :(")
    alert()
    input("press enter to continue")

