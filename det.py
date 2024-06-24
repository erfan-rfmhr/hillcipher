def laplace_expansion(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return val
    elif len(matrix) == 2:
        return matrix[0][0]
    elif len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for j in range(len(matrix)):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[:j] + matrix[j+1:]]
        sign = (-1) ** (j % 2)
        sub_det = laplace_expansion(sub_matrix)
        det += sign * matrix[0][j] * sub_det
    
    return det
