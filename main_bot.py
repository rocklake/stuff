import random
import string
import re
import time
from datetime import datetime
import threading
import os
#import joblib # ai
#import pandas as pd # ai
#model = joblib.load("2b2t_queue_model.pkl") # ai
msg = "i am currently AFK and this is a new feature i added to my custom client so if it breaks and starts spamming you sorry"
lcread = ""
queue_spot = 0
dm = 0
dp = 0
result = 0
def data():
    global lcread
    global dp
    global result
    while True:
        c = open("command.txt", "w", encoding='utf-8')
        c.write("queue")
        c.close()
        time.sleep(0.1)
        lc = open(r"lastchat2.txt" , "r", encoding='utf-8')
        lcread = lc.read()
        lc.close()
        if "2b2t queue lengths: normal: " in lcread:
            match = re.search(r'2b2t queue lengths: normal: (\d+)', lcread)
            if match:
                result = int(match.group(1))
                up = open("output.txt", "a", encoding='utf-8')
                now = datetime.now()
                day_of_week = now.strftime("%A")
                hour = now.hour
                minute = now.minute
                second = now.second
                up.write(str(result) + "  " + str(day_of_week) + "-" + str(hour) + ":" + str(minute) + ":" + str(second) + "\n")
                dp = dp + 1
                up.close()
                time.sleep(1.5)
            else:
                pass
        else:
            pass
def position_in_queue():
    global queue_spot
    while True:
        lc = open(r"lastchat.txt" , "r", encoding='utf-8')
        lcread = lc.read()
        lc.close()
        if "Position in queue: " in lcread:
            match = re.search(r'\d+', lcread)
            if match:
                queue_spot = int(match.group())
            else:
                pass
        else:
            pass
        time.sleep(1)
def afker():
    global dm
    rng = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    while True:
        lc = open(r"lastchat.txt" , "r", encoding='utf-8')
        lcread = lc.read()
        lc.close()
        if "whispers:" in  lcread:
            time.sleep(6)
            c = open(r"command.txt", "w")
            c.write("r " + msg + " " + rng)
            dm = dm + 1
            c.close()
            rng = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
            time.sleep(1)
            lcw = open(r"lastchat.txt", "w")
            lcw.write("not")
            lcw.close()
            time.sleep(6)
        time.sleep(0.05)

data_t = threading.Thread(target=data)
data_t.start()
position_in_queue_t = threading.Thread(target=position_in_queue)
position_in_queue_t.start()
afker_t = threading.Thread(target=afker)
afker_t.start()
print("startig...")
time.sleep(10)
queue_spot_start = queue_spot
start_time = time.time()
while True:
    time_now = time.time()
#    week = datetime.today().weekday() # ai
#    now = datetime.now() # ai
#    hour = now.hour # ai
#    minute = now.minute # ai
#    second = now.second # ai
#    if week < 5: # ai
#        is_weekend = 0 # ai
#    else: # ai
#        is_weekend = 1 # ai
#    X_input = pd.DataFrame([[is_weekend, hour, minute, second]], columns=["IsWeekend", "Hour", "Minute", "Second"]) # ai
#    prediction = model.predict(X_input) # ai
    prediction = [0.01, "null"] # no ai
    t2p = (queue_spot_start - queue_spot) / (time_now - start_time) * 60
    print("""
=========================
pos   :""", queue_spot , """
t2p   :""", t2p, """
ai    :""", prediction[0], """
ai_off:""", abs(float(prediction[0]) - result), """
dp    :""", dp ,"""
dm    :""", dm ,"""
=========================
logs:
""" + lcread)
    time.sleep(0.4)
    os.system("cls")
