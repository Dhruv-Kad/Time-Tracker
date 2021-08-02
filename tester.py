from datetime import datetime


dictionary = {}

while 1 == 1:
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S:%p")
    task = input("task: ")
    dictionary[task] = current_time

    if task == "exit":
        break


for key, value in dictionary.items():
    print(key, ' : ', value)
