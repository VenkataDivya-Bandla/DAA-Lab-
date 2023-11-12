#LAB-5
#ROWS With Most No of One's
def with_most_ones(matrix):
    max_ones = 0
    row_index = -1

    for i, row in enumerate(matrix):
        count_ones = row.count(1)
        if count_ones > max_ones:
            max_ones = count_ones
            row_index = i

    return row_index


matrix = [
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1]
]


print("Row index with the most ones:",with_most_ones(matrix) )


#Middle Row and Column Sum
def row_column_sum(matrix):
    n = len(matrix)
    middle = n // 2
    row_sum = sum(matrix[middle])
    col_sum = sum(row[middle] for row in matrix)

    return row_sum, col_sum


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sum, col_sum = row_column_sum(matrix)
print("Sum of the middle row:", row_sum)
print("Sum of the middle column:", col_sum)



