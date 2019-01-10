import re
import json
import operator

logFile = open("access.log", "r")
uidFile = open("uid.log", "w+")

for line in logFile.readlines():
    re_pattern = r'userid%22%3A%22(.*?)%22'
    match = re.search(re_pattern, line)
    if match:
        # print("Found UID: " + match.group(1))
        uidFile.write(match.group(1) + "\n")
        uid = uidFile.read(10)
        print(uid)
    else:
        pass
logFile.close()
uidFile.close()

uidFile = open("uid.log", "r")

dictionary_uid_counts = {}

for uidLine in uidFile.readlines():
    if not(uidLine in dictionary_uid_counts):
        dictionary_uid_counts[uidLine] = 1
    else:
        dictionary_uid_counts[uidLine] = int(dictionary_uid_counts.get(uidLine)) + 1

topFiveDictionary = dict(sorted(dictionary_uid_counts.items(), key=operator.itemgetter(1), reverse=True)[:5])

print(topFiveDictionary)

