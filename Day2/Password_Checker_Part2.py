import re

text_file = open("Input_Data.txt", "r")
lines = text_file.read().split("\n")
text_file.close()

def password_parser(text):
    """
    Parses the password to extract important info (start int, end int, character, password text.

    :param text: Expects data in format [number1]-[number2] [character]: [password text]
    :type text: String
    :return: Returns 4 values: number1, number2, character, and password text
    :rtype: list of ints and strings
    """
    int1, text = re.split("-", text, 1)
    int2, text = re.split("\s", text, 1)
    character, text = re.split(":", text, 1)
    password = text[1:] # Gets rid of the space in front (not actually necessary but I prefer it)
    return int(int1), int(int2), character, password

def is_correct_password(int1, int2, character, password):
    """
    Checks if the password contains the character at location int1 or int2. Assumes int1 and int2 are not
    out of bounds of the password

    :param int1: First character location
    :type int1: int
    :param int2: Second character location
    :type int2: int
    :param character: Single character to check in password
    :type character: char
    :param password: contains password text
    :type password: string
    :return: returns 1 if true, 0 if false
    :rtype: int (0 or 1)
    """
    if password[int1-1] == character and password[int2-1] == character:
        return 0
    elif password[int1-1] == character or password[int2-1] == character:
        return 1
    return 0

total_correct_passwords = 0
for password in lines:
    int1, int2, char, password = password_parser(password)
    total_correct_passwords += is_correct_password(int1, int2, char, password)
print(total_correct_passwords)