text_file = open("Input_Data.txt", "r")
lines = text_file.read().split("\n")
text_file.close()

data = list()
current_group = list()

for line in lines:
    if line != "":
        new_mem = set(line)
        current_group.append(new_mem)
    else:
        intersect = set(current_group[0])
        for item in current_group:
            intersect = intersect.intersection(item)
        if len(intersect) > 0:
            data.append(len(intersect))
        current_group = list()
intersect = set(current_group[0])
for item in current_group:
    intersect = intersect.intersection(item)
if len(intersect) > 0:
    data.append(len(intersect))

Sum = sum(data)
print(Sum)
