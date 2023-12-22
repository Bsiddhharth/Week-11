def dett(mat):
    if len(mat)!=len(mat[0]):
        return "must be sqr matrix"
    
    if len(mat)==1:
        return mat[0][0]
    
    det=0
    
    for col in range(len(mat[0])):
        cofact= mat[0][col] * dett(get_submat(mat,0,col))
        det+= ((-1)**col)*cofact
        
        
    return det

def get_submat(mat,row,col):
    return [[mat[i][j] for j in range(len(mat[i])) if j!=col ]for i in range(len(mat))if i!=row]  


# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
matrix=[[3,8],
        [4,6]]

result = dett(matrix)
print("Determinant of the matrix:")
print(result)

                