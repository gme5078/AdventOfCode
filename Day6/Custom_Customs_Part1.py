text_file = open("Input_Data.txt", "r")
lines = text_file.read().split("\n")
text_file.close()

data = list()
current_group = set()
for line in lines:
    if line != "":
        for char in line:
            current_group.add(char)
    else:
        data.append(len(current_group))
        current_group = set()
data.append(len(current_group))
Sum = sum(data)
print(Sum)
