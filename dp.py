def strassen_matrix_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    M3 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    M4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    M6 = strassen_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)
     
    result = []
    for i in range(mid):
        result.append(C11[i] + C12[i])
    for i in range(mid):
        result.append(C21[i] + C22[i])
    
    return result

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = strassen_matrix_multiply(A, B)
for row in result:
    print(row)