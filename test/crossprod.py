# def get_input(row,col):
#     res=[]
#     for i in range(row):
#         r=[]
#         for j in range(col):
#             r.append(float(input(f"ENter  the element at pos {i+1},{j+1}: ")))
#         res.append(r)
#     return res

# def cross_prod(mat1,mat2):
#     res=[[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1)) ]
    
#     for i in range(len(mat1)):
#         for j in range(len(mat2[0])):
#             res[i][j] = mat1[i][j] * mat2[i][j]
            
#     return res

# mat1=get_input(1,3)
# mat2=get_input(1,3)

# print(cross_prod(mat1,mat2))


def multi(mat1,mat2):
    row1=len(mat1)
    col1=len(mat1[0])
    
    row2=len(mat2)
    col2=len(mat2[0])
    
    if col1!=row2:
        return None
    
    res=[[0 for j in range(col2)] for i in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                res[i][j]+=mat1[i][k]*mat2[k][j]
    return res

def get_input(row,col):
    res=[]
    for i in range(row):
        r=[]
        for j in range(col):
            r.append(float(input(f"enter the element at pos {i+1}, {j+1} : ")))
        res.append(r)
        
    return res 

def print_mat(mat):
    for i in mat:
        print(i)
        


mat1=[[1,1,1],
      [1,1,1],
      [1,1,1]]
mat3=[[2,2,2],
      [2,2,2],
      [2,2,2]]   
print_mat(multi(mat1,mat3))

def add(mat1,mat2):
    res=[]
    for i in range(len(mat1)):
        r=[]
        for j in range(len(mat1[0])):
           r.append(mat1[i][j]+mat2[i][j])
        res.append(r)
    return res

print()
print_mat(add(mat1,mat3))


def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]

def deter(mat):
    if len(mat)!=len(mat[0]):
        return None
    
    if len(mat)==1:
        return mat[0][0]
    
    d=0
    for col in range(len(mat[0])):
        cofat=mat[0][col]*deter(get_submat(mat,0,col))
        d+=((-1)**col)*cofat 
        
    return d 


def get_submat(mat,row,col):
    return [[mat[i][j] for j in range(len(mat[0])) if j!=col] for i in range(len(mat)) if i!=row]


def adj(mat):
    if len(mat)!=len(mat[0]):
        return None

    cofact=[]
    for r in range(len(mat)):
        row=[]
        for c in range(len(mat[0])):
            cf=((-1)*(r+c))*deter(get_submat(mat,r,c))
            row.append(cf)
        cofact.append(row)    
        
    det=deter(mat)    
    adj=transpose(cofact)
    inverse=[[elmt/det for elmt in row ]for row in adj]
    return inverse


            

   
    




            
 
        
        
            