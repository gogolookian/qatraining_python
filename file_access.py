import re
import json

logFile = open("access.log", "r")
uidFile = open("uid.log", "w+")

for line in logFile.readlines():
    re_pattern = r'userid%22%3A%22(.*?)%22'
    match = re.search(re_pattern, line)
    if match:
        # print("Found UID: " + match.group(1))
        uidFile.write(match.group(1) + "\n")
    else:
        pass


print(uidFile.read())



logFile.close()

