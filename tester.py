import json
import time
from datetime import datetime
x = datetime.now().strftime("%a:%d:%b:%Y")
 #adds current day to the dictionary
dictionary = {x : "current_day",}


def task(taskname):
    start_time = time.time()
    #there was an if statment here, but I realized that you only don't really need to get this output
    input("Type anything to stop counting time: ")
    end_time = time.time()
    #gets time that passed
    time_passed = end_time - start_time
    #searches for existing task
    if taskname in dictionary:
#gets old task time
      oldtime = (dictionary.get(taskname))
# prints the time spent on the current iteration of the task
      print(time_passed)
#adds two times together
      time_passed += oldtime
    else:
#stores time passed in dictonary the first time
        dictionary[x] = time_passed
#prints time passed
        print(time_passed)
#stores time passed again
    dictionary[x] = time_passed

#inf loop
while True:
    x = input("enter taskname here:")
    if x == "stop" or "exit":
        break
    else:
        task(x)
#prints log of todays activity
for key, value in dictionary.items():
    print(key, ':', value)
#stores everyting to json
with open('myfile.json', 'w') as fp:
    json.dump(dictionary, fp)

        
    
    

