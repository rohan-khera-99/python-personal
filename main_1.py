import simplejson
# importing os to see the file stats
import os

if os.path.isfile("./test_1.json") and os.stat("./test_1.json").st_size != 0:
    file = open("./test_1.json", "r+")
    # will load and read the data from the file
    dat = simplejson.loads(file.read())
    print("number is ", dat["num"], "adding 1 to it")
    dat["num"] = int(dat["num"] + 1)
    print("new number is: ", dat["num"])
# if the file dosent exist we create one
else:
    file = open("./test_1.json", "w+")
    dat = {"name": "rk:", "num": "11"}
    print("NO file found, creating a file and setting number to: ", dat["num"])

file.seek(0)
file.write(simplejson.dumps(dat))