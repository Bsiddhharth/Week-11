def get_input(row,col):
    res=[]
    for i in range(row):
        r=[]
        for j in range(col):
            ele=float(input(f"Enter the elemant at index {i+1},{j+1} : "))
            r.append(ele)
        res.append(r)
    return res        

def add(mat1,mat2):
    row=len(mat1)
    col=len(mat1[0])
    
    if row==len(mat2) and col==len(mat2[0]):
        res=[]
        for i in range(row):
            r=[]
            for j in range(col):
                r.append(mat1[i][j]+mat2[i][j])
            res.append(r)        
        return res
    return "not a sqr matrix"

def mult(mat1,mat2):
    row1=len(mat1)
    col1=len(mat1)
    
    row2=len(mat2)
    col2=len(mat2)
    
    if col1!=row2:
        return "cant perform multiplication"
    
    res=[[0 for _ in range(col2)]for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                res[i][j]=mat1[i][k]*[k][j]
                
    return res                   
    
    
def print_mat(mat):
    for i in mat:
        print(i)
                
def transpose(mat):
    return [[mat[j][i] for j in  range(len(mat))]for i in range(len(mat[0]))]

def determinant(mat):
    if len(mat)!=len(mat[0]):
        return "Not a sqr matrix"
    
    d=0
    for col in range(len(mat[0])):
        cofact=mat[0][col] * determinant(get_submat(mat,0,col))
        d+=cofact*((-1)**col)
        
    return d

def get_submat(mat,row,col):
    return [[mat[i][j] for j in range(len(mat[0])) if j!=col] for i in range(len(mat)) if i!=row] 


def adj_mat(mat):
    if len(mat)!=len(mat[0]):
        return "Not a sqr matrix"
    
    cofact=[]
    for r in range(len(mat) ):
        row=[]
        for c in range(len(mat[0])) :
            cofac=((-1)**(r+c) )* determinant(get_submat(mat,r,c))
            row.append(cofac)
        cofact.append(row) 
        
    det=determinant(mat)
    adj=transpose(cofact)
    # return adj
    return [[elmnt/det for elmnt in row] for row in adj]      #inverse 
            
                               
def trace(mat):
    c=0
    
    if len(mat)!=len(mat[0]):
        return "Not a sqr matrix"
    for i in range(len(mat)):
       c+=mat[i][i]
       
    return c   
                