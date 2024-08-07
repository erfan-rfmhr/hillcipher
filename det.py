def laplas_diag_method(matrix):
    if len(matrix) == 2 :
        val = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return val
    elif len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for j in range(len(matrix)):

        sub_matrix = [[0 for col in range(len(matrix)-1)] for row in range(len(matrix)-1)]

        row= 0
        for i in matrix[1:]:
            sub_matrix[row] = i[:j] + i[j+1:]
            row+=1

        sign = (-1) ** (j % 2)  
        sub_det = laplas_diag_method(sub_matrix)
        det += sign * matrix[0][j] * sub_det
    
    return det

