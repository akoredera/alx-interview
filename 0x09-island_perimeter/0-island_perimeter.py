#!/usr/bin/python3
'''
island perimeter
'''

def island_perimeter(grid):
    '''
    island perimeter
    '''
    new_list = []
    for i in range(len(grid)):
        for row in grid:
            if i > 0 and i < len(grid):
                if row != grid[0] and row != grid[-1]:
                    new_list.append(row[i])
    return len(new_list)