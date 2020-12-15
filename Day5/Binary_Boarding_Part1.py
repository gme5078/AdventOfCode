import math

text_file = open("Input_Data.txt", "r")
lines = text_file.read().split("\n")
text_file.close()

def get_seat_position(min_value, max_value, boarding_pass):
    """
    Uses a binary search to find boarding pass position

    :param min_value: min boarding pass seat
    :type min_value: Int
    :param max_value: max boarding pass seat
    :type max_value; Int
    :param boarding_pass: Boarding Pass
    :type boarding_pass: String
    :return: returns row or column position
    :rtype: Int
    """
    if len(boarding_pass) == 0:
        return max_value
    else:
        next_move = boarding_pass[0]
        boarding_pass = boarding_pass[1:]
        if next_move == "F" or next_move == "L":
            middle_bottom = math.floor((max_value - min_value) / 2) + min_value
            return get_seat_position(min_value, middle_bottom, boarding_pass)
        else:
            middle_top = math.ceil((max_value - min_value) / 2) + min_value
            return get_seat_position(middle_top, max_value, boarding_pass)

max_seatID = 0
for line in lines:
    seatID = get_seat_position(0, 127, line[:7]) * 8 + get_seat_position(0, 7, line[7:])
    max_seatID = max(max_seatID, seatID)
print(max_seatID)