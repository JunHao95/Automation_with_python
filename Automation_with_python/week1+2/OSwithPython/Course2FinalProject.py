#!/usr/bin/env python3

import re
import operator
import json
Errors_dict ={}
per_user = {}

with open('syslog.log','r') as fiLe:
    for line in fiLe:
        if re.search(r"ticky: ERROR ([\w ]*) ",line):
            result = re.search(r"ticky: ERROR ([\w ]*) ",line)
            index = re.search(r"\(([A-Za-z0-9_]+)\)",line)
            if index:
                username = line[index.start() +1:index.end() -1]
                if username in per_user:
                    per_user[username]["ERROR"] += 1
                else:
                    per_user[username] = {"INFO":0,"ERROR":0}
                    per_user[username]["ERROR"] = 1
            if result:
                error_type = line[result.start() + 13: result.end()]
                if error_type in Errors_dict:
                    Errors_dict[error_type] += 2
                else:
                    Errors_dict[error_type] = 1

        elif re.search(r"ticky: INFO ([\w ]*) ",line):
            index = re.search(r"\(([A-Za-z0-9_]+)\)",line)
            if index:
                username = line[index.start() +1:index.end() -1]
                if username in per_user:
                    per_user[username]["INFO"] += 1
                else:
                    per_user[username] = {"INFO":0,"ERROR":0}
                    per_user[username]["ERROR"] = 1
fiLe.close()

final_errorDict = sorted(Errors_dict.items() , key=operator.itemgetter(1))
user = sorted(per_user.items(), key=operator.itemgetter(0))

#print("Final error DICT is {} \n User Dict is {}".format(final_errorDict,user))

with open("user_statistics.csv","w") as f:
    f.write("Username,INFO,ERROR\n")
    for i in user:
        string = str(i)
        print("Unformatted is ",str(i))
        new = re.sub('[^A-Za-z0-9, ]+', '', string)
        new1 = re.sub('INFO', '', new)
        new2 = re.sub('ERROR', '', new1)
        print("Formatted is",new2)
        f.write(new2 +"\n")

f.close()


with open("error_message.csv","w") as f1:
    f1.write("ERROR,Count\n")
    for i in final_errorDict:
        string = str(i)
        new = re.sub('[^A-Za-z0-9, ]+', '', string)
        #print("With strip is",new)
        f1.write(new +"\n")

f1.close()

