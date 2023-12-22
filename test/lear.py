row1=int(input(f"Enter the number of rows of mat1: "))
col1=int(input(f"Enter the number of cols of mat1: "))

# row2=int(input(f"Enter the number of rows of mat2: "))
# col2=int(input(f"Enter the number of cols of mat2: "))

def get_input(row,col):
    res=[]
    for i in range(row):
        r=[]
        for j in range(col):
            ele=float(input(f"ENter the elements in pos {i+1},{j+1} : "))
            r.append(ele)
        res.append(r)
        
    return res

def addd(mat1,mat2):
    row=len(mat1)
    col=len(mat1[0])
    
    res=[]
    
    if row!=len(mat2) and col!=len(mat2[0]):
        return "not a square matrix"
    
    for i in range(row):
            r=[]
            for j in range(col):
                r.append(mat1[i][j]+mat2[i][j])
            res.append(r)    
    disp(res)

def sub(mat1,mat2):
    row=len(mat1)
    col=len(mat1[0])
    
    res=[]
    
    if row!=len(mat2) and col!=len(mat2[0]):
         return "not a square matrix"
        
    for i in range(row):
            r=[]
            for j in range(col):
                r.append(mat1[i][j] - mat2[i][j])
            res.append(r)    
    disp(res)
                   
    
def disp(mat):
    for i in mat:
        print(i)
        
        
print("\n enter the matrix1: \n")
mat1=get_input(row1,col1)

# print("\n enter the matrix2: \n")
# mat2=get_input(row2,col2)    

print()
disp(mat1)

# print()
# disp(mat2)

# print("ADD")
# print(addd(mat1,mat2))

# print("SUB")
# print(sub(mat1,mat2))

def mul(mat1,mat2):
    row1=len(mat1)
    col1=len(mat1[0])
    
    
    row2=len(mat2)
    col2=len(mat2[0])
    
    res=[[0 for _ in range(col2)] for _ in range(row1)] 
    
    if col1==row2:
        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    res[i][j]+=mat1[i][k]*mat2[k][j]
                    
        return res 
    return None

# print("mul")
# disp(mul(mat1,mat2))

# ---------------------------------------------------------------------                        

def tra(mat):
    row=len(mat)
    col=len(mat[0])
    
    tr=[[0 for i in range(row)] for j in range(col)]
    
    for i in range(row):
        for j in range(col):
            tr[j][i]=mat[i][j]
           
    return tr        
            
print()
t=tra(mat1)
for i in t:
    print(i)            
        
# ----------------------------------------------------------------------------   
# tracec is the sum of main diagonal elements

def trace(mat):
    trace=0
    if len(mat)== len(mat[0]):
        for i in range(len(mat)):
           trace+=mat[i][i]
        return trace
    return "Not sqr matrix"    
# ----------------------------------------------------------------------------------

def deter(mat):
    if len(mat)!=len(mat[0]):
        return "must be sqr matrix"
    
    if len(mat)==1:
        return mat[0][0]
    
    det=0
    for col in range(len(mat[0])):
        cofat=mat[0][col]*deter(get_submat(mat,0,col))
        det+= ((-1)**col)*cofat
        
    return det

def get_submat(mat,row,col) :
    return [[mat[i][j] for j in range(len(mat[i]))if j !=col]for i in range(len(mat)) if i!=row]

mat=[[3,8],[4,6]]

print(deter(mat))



