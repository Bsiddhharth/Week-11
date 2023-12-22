row1=int(input(f"Enter the rows of mat1: "))
col1=int(input(f"Enter the cols of mat1: "))

row2=int(input(f"Enter the rows of mat2: "))
col2=int(input(f"Enter the cols of mat2: "))


# def get_input(row,col):
#     mat=[]
#     for i in range(row):
#         r=[]
#         for j in range(col):
#             ele=float(input(f"Enter the element at pos {i+1},{j+1} : "))
#             r.append(ele)
#         mat.append(r)
        
#     return mat

# print("Enter matrix 1: ")
# mat1=get_input(row1,col1)

# print("Enter matrix 2: ")
# mat2=get_input(row2,col2)

# def printt(maat):
#     for i in maat:
#         print(i)
    
# printt(mat1)
# print()
# printt(mat2)    

# print(len(mat1))
# print(len(mat1[0]))

# # def multi(mat1,mat2):
# # len(mat[0]) gives the number of column  
# # len(mat) give sthe number of rows    

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
#                     res[i][j]+=mat1[i][k]*mat2[k][j]
#         return res 
    
#     return False

# m=multi(mat1,mat2)           
# for i in m:
#     print(i)


def get_input(row,col):
    
    res=[]
    
    if row!=col:
        return
    
    for i in range(row):
        r=[]
        for j in range(col):
            r.append(float(input(f"Enter the element at pos{i+1}, {j+1} : ")))
            
        res.append(r)
        
    return res 

def add(mat1,mat2):
    row=len(mat1)
    col=len(mat2)
    if row!=len(mat2) and col!=len(mat2[0]):
        return None
    res=[]
    for i in range(row):
        r=[]
        for j in range(col):
            r.append(mat1[i][j]+mat2[i][j])
        res.append(r)
        
    return res

def multi(mat1,mat2):
    row1=len(mat1) 
    col1=len(mat1[0]) 
    
    row2=len(mat2) 
    col2=len(mat2[0])   
    
    if col2!= row1:
        return     None
    
    res=[[0 for _ in range(col2)] for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2) :
            for k in range(col1):
                res+= mat1[i][k]*mat2[k][j]
    return res            
    
    
       
        
        
        
