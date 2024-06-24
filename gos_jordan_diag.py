# def evaluate_diag(matrix , rows , cols):
#     diag = 0
#     for row in range(rows):
#         for col in range(col):
#             if row == col:
                

from copy import deepcopy
def GosJordan_diag(matrix):
    copy_matrix = deepcopy(matrix)

    row , col = len(matrix) , len(matrix[0])
    print(copy_matrix[0][0])
    
    for i in range(min(row,col)):
        main_row = i

        for j in range(i+1 , row):

            # if abs(copy_matrix[j , i])> abs(copy_matrix[main_element,i]):
            if abs(copy_matrix[j][i])> abs(copy_matrix[main_row][i]):
                main_row = j

# --------------------

        if main_row != i:

            temp = copy_matrix[i] 
            copy_matrix[i] = copy_matrix[main_row]
            copy_matrix[main_row] = temp
        
        main_element = copy_matrix[i][i]
        if main_element != 0 :
            for j in range((len(copy_matrix[i]))):
                copy_matrix[i][j] //= float(main_element)
                # copy_matrix[i][j] /= main_element

        for j in range(row):
            if j != i:
                factor = copy_matrix[j][i] / copy_matrix[i][i] if copy_matrix[i][i] != 0 else 0
                # A[j, :] -= factor * A[i, :]
                for k in range(len(copy_matrix[j])):
                    copy_matrix[j][k] = copy_matrix[j][k] - (factor * copy_matrix[i][k])
        
    # evaluate_diag(copy_matrix , row , col)
    print(copy_matrix)
            # copy_matrix[]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dig = GosJordan_diag(matrix)