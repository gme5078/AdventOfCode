import pandas as pd

# Read data and split each char into separate cell
data = pd.read_csv('Input_Data.txt', header=None)
data = data[0].apply(lambda x: pd.Series(list(x)))

def num_trees_hit(right, down):
    row_index = 0
    col_index = 0
    trees_hit = 0
    while row_index + 1 < data.shape[0]:
        row_index += down
        col_index += right
        if data.iloc[row_index, col_index % data.shape[1]] == "#":
            trees_hit += 1
    return trees_hit

right_1_down_1 = num_trees_hit(1, 1)
right_3_down_1 = num_trees_hit(3, 1)
right_5_down_1 = num_trees_hit(5, 1)
right_7_down_1 = num_trees_hit(7, 1)
right_1_down_2 = num_trees_hit(1, 2)

print(right_1_down_1*right_1_down_2*right_3_down_1*right_5_down_1*right_7_down_1)
