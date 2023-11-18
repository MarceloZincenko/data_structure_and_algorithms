#73. Set Matrix Zeroes
def setZeroes(matrix):
    zeroRows = set()
    zeroCols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeroRows.add(i)
                zeroCols.add(j)
    
    for i in zeroRows:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0

    for j in zeroCols:
        for i in range(len(matrix)):
            matrix[i][j] = 0