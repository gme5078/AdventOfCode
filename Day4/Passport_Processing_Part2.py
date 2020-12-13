import re
import pandas as pd

text_file = open("Input_Data.txt", "r")
lines = text_file.read().split("\n")
text_file.close()

column_names = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
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

def is_valid_birth_year(value):
    """
    Checks if the year is between 1920 and 2002

    :param value: Could technically be anything
    :return: True or False
    """
    if pd.isnull(value):
        return False
    value = int(value)
    if 1920 <= value <= 2002:
        return True
    return False

def is_valid_issue_year(value):
    """
    Checks if the year is between 2010 and 2020

    :param value: Could technically be anything
    :return: True or False
    """
    if pd.isnull(value):
        return False
    value = int(value)
    if 2010 <= value <= 2020:
        return True
    return False

def is_valid_expiration_year(value):
    """
    Checks if the year is between 2020 and 2030

    :param value: Could technically be anything
    :return: True or False
    """
    if pd.isnull(value):
        return False
    value = int(value)
    if 2020 <= value <= 2030:
        return True
    return False

def is_valid_height(value):
    """
    Checks if the height follows format of 59in-76in or 150cm-193cm

    :param value: Could technically be anything
    :return: True or False
    """
    if pd.isnull(value):
        return False
    last_chars = value[-2:]
    first_chars = value[:-2]
    if first_chars.isdigit():
        first_chars = int(first_chars)
    else:
        return False

    if last_chars == "in":
        if 59 <= first_chars <= 76:
            return True
    if last_chars == "cm":
        if 150 <= first_chars <= 193:
            return True
    return False

def is_valid_hair(value):
    """
    Checks if the hair color is valid format: #[a-f0-9]{6}

    :param value: Could technically be anything
    :return: True or False
    """
    if pd.isnull(value):
        return False
    matches = re.findall("#[a-f0-9]{6}", value)
    if len(matches) > 0 and len(value) == 7:
        return True
    return False

def is_valid_eye_color(value):
    """
    Checks if the eye color is one of these: ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    :param value: Could technically be anything
    :return: True or False
    """
    if pd.isnull(value):
        return False
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if value in eye_colors:
        return True
    return False

def is_valid_ID(value):
    """
    Checks if the PID is nine digits

    :param value: Could technically be anything
    :return: True or False
    """
    if pd.isnull(value):
        return False
    matches = re.findall("[0-9]{9}", value)
    if len(matches) > 0 and len(value) == 9:
        return True
    return False

count = 0
for index, row in df.iterrows():
    # Ridiculous if statement
    if is_valid_birth_year(row["byr"]) and is_valid_expiration_year(row["eyr"]) and\
        is_valid_issue_year(row["iyr"]) and is_valid_ID(row["pid"]) and\
        is_valid_eye_color(row["ecl"]) and is_valid_height(row["hgt"]) and\
        is_valid_hair(row["hcl"]):
        count += 1

print(count)