import re
import pandas as pd

text_file = open("Input_Data.txt", "r")
lines = text_file.read().split("\n")
text_file.close()

column_names = ["byr", "iyr", "eyr","hgt","hcl","ecl","pid","cid"]
df = pd.DataFrame(columns=column_names)

curr_passport = {}
for line in lines:
    items = re.split("\s", line, 8)
    if items[0] != "":
        for item in items:
            key, value = re.split(":", item, 1)
            curr_passport[key] = value
    else:
        df = df.append(curr_passport, ignore_index=True)
        curr_passport = {}
df = df.append(curr_passport, ignore_index=True)

count = 0
for index, row in df.iterrows():
    num_missing = row.isnull().sum()
    if num_missing == 0:
        count += 1
    elif num_missing == 1 and pd.isnull(row["cid"]):
        count += 1

print(count)