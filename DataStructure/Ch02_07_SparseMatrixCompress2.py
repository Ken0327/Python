def restore(sparse):
    row = sparse[0][0]
    column = sparse[0][1]
    array = [[0] * column for i in range(row)]
    k = 1
    for i in range(row):
        for j in range(column):
            if k <= sparse[0][2] and \
               i == sparse[k][0] and j == sparse[k][1]:
               array[i][j] = sparse[k][2]
               k += 1
            else:
                array[i][j] = 0
    return array

sparse = [
             [5, 6, 4], 
             [1, 1, 3], 
             [2, 3, 6],
             [3, 2, 9], 
             [4, 4, 12]
          ]

array = restore(sparse)
print(array)