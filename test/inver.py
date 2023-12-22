def print(mat):
    for i in mat:
        print(i)
        
def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]        

def determinant(mat):
    if len(mat)!=len(mat[0]):
        return None
    if len(mat)==1:
        return mat[0][0]
    
    d=0
    for col in range(mat[0]):
        cofact=mat[0][col] * determinant(get_submat(mat,0,col))
        d+=((-1)**col)*cofact
        
    return d 

def get_submat(mat,row,col):
    return [[mat[i][j] for j in range(len(mat[0])) if j!=col] for i in range(len(mat)) if i!=row]

 
def adj(mat):
    if len(mat)!=len(mat[0]):
        return    
    
    cofact=[]
    for r in range(len(mat)):
        row=[]
        for c in range(len(mat[0])):
            cf=((-1)*(r+c)) * determinant(get_submat(mat,r,c))  #laplace explansion
            row.append(cf)
        cofact.append(row)
       
    det=determinant(mat)    
    adj=transpose(cofact)        
    
    inverse=[[elmnt/det for elmnt in row] for row in adj]
    return  inverse