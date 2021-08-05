import json
import time
from collections import defaultdict
from datetime import datetime
result = defaultdict(int)
x = datetime.now().strftime("%a:%d:%b:%Y")
 
dictionary = {} 


def task(taskname):
    start_time = time.time() 
    input("Type anything to stop counting time: ")
    end_time = time.time()
    time_passed = end_time - start_time
    if taskname in dictionary:
      oldtime = (dictionary.get(taskname))
      print(time_passed)
      time_passed += oldtime
    else:
        dictionary[x] = time_passed
        print(time_passed)

    dictionary[x] = time_passed


while 1 == 1:
    x = input("enter taskname here:")
    if x == "stop":
        break
    else:
        task(x)

for key, value in dictionary.items():
    print(key, ':', value)

with open('myfile.json, "w"') as fp:
    json.dump(dictionary, fp)

        
    
    

