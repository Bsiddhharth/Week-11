# def print_matrix(matrix):
#     for row in matrix:
#         print(row)

# def transpose(matrix):
#     # Transpose the matrix
#     return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# # def matrix_minor(matrix, row, col):
# #     # Return the minor of the matrix after removing the specified row and column
# #     return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

# def matrix_minor(mat,row,col):
#     return [[mat[i][j] for j in range(len(mat[i])) if j!=col ]for i in range(len(mat))if i!=row]  

# # def determinant(matrix):
# #     # Base case for 2x2 matrix
# #     if len(matrix) == 2 and len(matrix[0]) == 2:
# #         return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# #     det = 0
# #     for c in range(len(matrix)):
# #         det += ((-1) ** c) * matrix[0][c] * determinant(matrix_minor(matrix, 0, c))
# #     return det

# def determinant(mat):
#     if len(mat)!=len(mat[0]):
#         return "must be sqr matrix"
    
#     if len(mat)==1:
#         return mat[0][0]
    
#     det=0
    
#     for col in range(len(mat[0])):
#         cofact= mat[0][col] * determinant(matrix_minor(mat,0,col))
#         det+= ((-1)**col)*cofact
#     return det    

# def adjoint_matrix(matrix):
#     # Check if the matrix is square
#     if len(matrix) != len(matrix[0]):
#         raise ValueError("Matrix is not square. Adjoint does not exist.")

#     # Calculate the cofactor matrix
#     cofactors = []
#     for r in range(len(matrix)):
#         row = []
#         for c in range(len(matrix[0])):
#             minor = matrix_minor(matrix, r, c)
#             cofactor = ((-1) ** (r + c)) * determinant(minor)
#             row.append(cofactor)
#         cofactors.append(row)

#     # Transpose the cofactor matrix to get the adjoint
#     adjoint = transpose(cofactors)

#     return adjoint

# # Example usage
# # if __name__ == "__main__":
#     # Replace this matrix with the one you want to find the adjoint of
#     # example_matrix = [[1, 2],
#     #                   [3, 4]]
# example_matrix=[ [1,2,-2,],
#                      [-1,3,0],
#                      [0,-2,1] ]
    
    
#     # try:
# result = adjoint_matrix(example_matrix)
# # print("Original Matrix:")
# # print_matrix(example_matrix)
# # print("\nAdjoint Matrix:")
# print_matrix(result)
#     # except ValueError as e:
#     #     print(e)



# def determinant(mat):
#     if len(mat)!=len(mat[0]):
#         return "must be sqr matrix"
    
#     if len(mat)==1:
#         return mat[0][0]
    
#     det=0
    
#     for col in range(len(mat[0])):
#         cofact= mat[0][col] * determinant(matrix_minor(mat,0,col))
#         det+= ((-1)**col)*cofact
        
        
#     return det

# def matrix_minor(mat,row,col):
#     return [[mat[i][j] for j in range(len(mat[i])) if j!=col ]for i in range(len(mat))if i!=row]  



def print_mat(mat):
    for i in mat:
        print(i)
        

def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]        


def determinant(mat):
    if len(mat)!=len(mat[0]):
        return "not a sqr matrix"
    
    if len(mat)==1:
        return mat[0][0]
    
    d=0
    for col in range(len(mat[0])):
        cofact=mat[0][col] * determinant(get_submat(mat,0,col))
        d+=((-1)**col)*cofact
        
    return d

def get_submat(mat,row,col):
    return [[mat[i][j] for j in range(len(mat[0])) if j!=col]for i in range(len(mat)) if i!=row] 

def adj_mat(mat):
    if len(mat)!=len(mat[0]):
        return "not a square matrix"
    
    cofact=[]
    for r in range(len(mat)):
        row=[]
        for c in range(len(mat[0])):
            cofactor=((-1)**(r+c))*determinant(get_submat(mat,r,c))
            row.append(cofactor) 
        cofact.append(row)
       
    # return transpose(cofact)
    det=determinant(mat)
    adj=transpose(cofact)
    return [[elmt / det for elmt in row]for row in adj]

matrix=[ [1,2,-2,],
         [-1,3,0],
          [0,-2,1] ]

print_mat(adj_mat(matrix))
    
                   
        
