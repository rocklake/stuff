import time
import random
import string
msg = "i am currently AFK and this is a new feature i added to my custom client so if it breaks and starts spamming you sorry"
rng = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
print("r " + msg + " " + rng)
while True:
    lc = open(r"lastchat.txt" , "r", encoding='utf-8')
    lcread = lc.read()
    lc.close()
    if "whispers:" in  lcread:
        print(lcread)
        time.sleep(6)
        c = open(r"command.txt", "w")
        c.write("r " + msg + " " + rng)
        c.close()
        rng = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
        time.sleep(1)
        lcw = open(r"lastchat.txt", "w")
        lcw.write("not")
        lcw.close()
        time.sleep(6)
    time.sleep(0.05)