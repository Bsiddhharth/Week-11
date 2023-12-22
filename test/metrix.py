def get_input(row,col):
    mat=[]
    
    for i in range(row):
        r=[]
        for j in range(col):
            ele=float(input(f"Enter the element at pos {i+1},{j+1} : "))
            r.append(ele)
        mat.append(r)
        
    return mat

def addd(mat1,mat2):
    c=[]        
    for i in range(row):
        v=[]
        for j in range(cols):
            v.append(mat1[i][j] + mat2[i][j])
        c.append(v)
    print(f"sum of mat1 and mat2: ")    
    for i in c:
        print(i)
        
        
def sub(mat1,mat2):     
    c=[]        
    for i in range(row):
        v=[]
        for j in range(cols):
            v.append(mat1[i][j] - mat2[i][j])
        c.append(v)
    print(f"differenece of mat1 and mat2: ")    
    for i in c:
        print(i)

row=int(input(f"ENter the number of rows: ")) 
cols=int(input(f"ENter the number of cols: ")) 

mat1=get_input(row,cols)

print()
mat2=get_input(row,cols)

print("matrix1: ")
for i in mat1:
    print(i)
    
print("matrix2: ")
for i in mat2:
    print(i)
    
addd(mat1,mat2)
sub(mat1,mat2)





    
               
    
 
   
 
    
    
        
        
                
