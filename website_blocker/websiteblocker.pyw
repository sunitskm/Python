import time
from datetime import datetime as dt
temp_host = r"E:\Python code\website_blocker\hosts"
final_host = r"C:\Windows\System32\drivers\etc\hosts"
blocked_sites = ["www.facebook.com","facebook.com"]
redirect_url = "127.0.0.1"
while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,13)):
        print("Working hours")
        with open(final_host,'r+') as f:
            content = f.read()
            #print("Inside open")
            for items in blocked_sites:
                #print(items)
                if items in content:
                    #print("Achi" + items)
                    #print(content)
                    pass
                else:
                    #print("Nai"+ items)
                    f.write(redirect_url + " " + items + "\n")

    else:
        with open(final_host,'r+') as f:
            content = f.readlines()
            f.seek(0)
            #new_content = []
            for items in content:
                #print(items)
                if not(any([i in items for i in blocked_sites])):
                    #print("Nai\n")
                    f.write(items)
                #else:
                    #print("Achi\n" + items)
            #print(new_content)
            f.truncate()
        print("Enjoy sanga!!")
    time.sleep(5)
