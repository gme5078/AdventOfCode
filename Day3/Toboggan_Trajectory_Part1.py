import pandas as pd

# Read data and split each char into separate cell
data = pd.read_csv('Input_Data.txt', header=None)
data = data[0].apply(lambda x: pd.Series(list(x)))


row_index = 0
col_index = 0
trees_hit = 0
while row_index + 1 < data.shape[0]:
    row_index += 1
    col_index += 3
    if data.iloc[row_index, col_index % data.shape[1]] == "#":
        trees_hit += 1

print(trees_hit)

