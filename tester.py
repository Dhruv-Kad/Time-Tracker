from datetime import datetime
import json


dictionary = {}
now = datetime.now()
x = "resume"

dictionary["Entry date"] = now.strftime("%a:%d:%b:%Y")

while x  == "resume":
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S:%p")
    task = input("task: ")
    dictionary[task] = current_time
    if task == "exit":
        break
    if task == "pause":
        x = 0
        x = input("To resume type resume, to exit type exit:")

with open('myfile.json', 'w') as fp:
    json.dump(dictionary, fp)
for key, value in dictionary.items():
    print(key, ' : ', value)



