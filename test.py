import json

with open("records.json", "r") as records:
    data = json.load(records)

user_map = {}
for user, d in data.items():
    day_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = int(d['start_time'])
    for day in day_array:
        if index <= int(d['end_time']):
            day_array[index] = 1
            index += 1
            user_map.update({user: day_array})

jsmith = user_map['jsmith']
jdoe = user_map['jdoe']
for v in range(23):
    jsmith[v] += jdoe[v]
    v += 1
for x in range(23):
    if jsmith[x] > 0:
        jsmith[x] = 1
i = 0
beginArray = []
endArray = []
while i in range(23):
    if jsmith[i] == jsmith[i + 1]:
        i += 1
    elif jsmith[i] == 1 and jsmith[i+1] == 0:
        beginArray.append(i)
        i += 1
    elif jsmith[i] == 0 and jsmith[i+1] == 1:
        endArray.append(i)
        i += 1

indexArray = []
if endArray[0] > beginArray[0]:
    beginArray[len(beginArray)] = endArray[0]
    for j in range(len(beginArray) - 1):
        indexArray[j] = (10 * beginArray[j] + endArray[j + 1])
else:
    indexArray[j] = (10 * beginArray[j] + endArray[j])

pass
