#48. Rotate Image
def rotate(matrix):

    right = 1

    for row in range(len(matrix)):
        
        for col in range(0, right):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col] 
        right += 1
    
    for row in range(len(matrix)):
        matrix[row] = matrix[row][::-1]