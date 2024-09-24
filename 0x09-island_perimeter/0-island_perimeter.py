#!/usr/bin/python3
'''
island perimeter
'''

# def island_perimeter(grid):
#     '''
#     island perimeter
#     '''
#     new_list = []
#     for i in range(len(grid)):
#         for row in grid:
#             if i > 0 and i < len(grid):
#                 if row != grid[0] and row != grid[-1]:

#                     new_list.append(row[i])
#     return len(new_list)
def check_val(x):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if (x == 0):
        return 1
    return 0


def island_perimeter(grid):
    """_summary_

    Args:
        grid (_type_): _description_
    """

    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    x = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i-1][j])
                if j-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i][j-1])

                try:
                    x += check_val(grid[i+1][j])
                except IndexError:
                    x += 1
                try:
                    x += check_val(grid[i][j+1])
                except IndexError:
                    x += 1

    return x