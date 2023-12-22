# row=int(input("Enter the number of rows:"))
# col=int(input("entr the number of cols:"))

# def get_input(row,col):
#     res=[]
#     for i in range(row):
#         r=[]
#         for  j in range(col):
#             ele=float(input(f"ENtert the element at pos {i+1} , {j+1} : "))
#             r.append(ele)
#         res.append(r) 
        
# def addd(mat1,mat2):
#     row=len(mat1)
#     col=len(mat1[0])
    
#     if row == len(mat2) and col==len(mat2[0]):
#          res=[]
#          for i in range(row):
#              r=[]
#              for j in range(col):
#                 r.append(mat1[i][j] + mat2[i][j] )
#              res.append(r) 
#          return res 
#     return  
    
# def sub(mat1,mat2):
#     row=len(mat1) 
#     col=len(mat1[0])
    
#     if row== len(mat2) and col==len(mat2[0]):
#         res=[]
#         for i in range(row):
#             r=[]
#             for j in range(col):
#                 r.append(mat1[i][j]-mat2[i][j])
#             res.append(r)
#         return res 
    
# row1=int(input("Enter the number of rows of matrix 1 : "))
# col1=int(input("Enter the number of cols of matrix 1: "))

# row2=int(input("Enter the number of rows of matrix 2 : "))
# col2=int(input("Enter the number of cols of matrix 2: "))

# def multi(mat1,mat2):
#     row1=len(mat1)    
#     col1=len(mat1[0])
       
#     row2=len(mat2)    
#     col2=len(mat2[0])
    
#     if col1==row2:
#         res=[[0 for _ in range(col2)]for _ in range(row1)]
#         for i in range(row1):
#             for j in range(col2):
#                 for k in range(col1):
#                     res[i][j]+=mat1[i][k]+mat2[k][j]
#         return res
#     return "cant multiply"    
    
    
# def transpose(mat):
#     return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

# def deter(mat):
#     if len(mat)!=len(mat[0]):
#         return "not a sqr matrix"
    
#     if len(mat)==1:
#         return mat[0][0]
    
#     det=0
#     for col in range(mat[0]):
#         confat=mat[0][col]  * deter(get_submat(mat,0,col)) 
#         det+=((-1)**col)*confat
        
#     return det

# def get_submat(mat,row,col):
#     return [[mat[i][j] for j in range(len(mat[i])) if j!=col]for i in range(len(mat)) if i!=row]

        
# --------------------------------------------------------------------------------------------------           
#inverse
        
def print_mat(mat):
    for row in mat:
        print(row)
        
def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]

def determinant(mat):
    if len(mat)!=len(mat[0]):
        return "Not square"
    
    if len(mat)==1:
        return mat[0][0]
    
    det=0
    for col in range(len(mat[0])):
        confact=mat[0][col] * determinant(matrix_minor(mat,0,col))
        det+=((-1)**col)*confact
    return det

def  matrix_minor(mat,row,col):
    return [[mat[i][j] for j in range(len(mat[i]))if j!=col]for i in range(len(mat))if i!=row]
    
def adj_mat(mat):
    if len(mat)!=len(mat[0]):
        return "not a sqr matrix"
    
    det=determinant(mat)
    
    cofact=[]
    for r in range(len(mat)):
        row=[]
        for c in range(len(mat[0])):
            cofactor=((-1)**(r+c))*determinant(matrix_minor(mat,r,c))
            row.append(cofactor)
        cofact.append(row)
        
    adj=transpose(cofact)
    inverse = [[element / det for element in row] for row in adj]

    # return inverse
    # return adj    


matrix=[ [1,2,-2,],
         [-1,3,0],
          [0,-2,1] ]

print_mat(adj_mat(matrix))
    