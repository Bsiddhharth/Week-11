# def get_input(row,col):
#     res=[]
#     for i in range(row):
#         r=[]
#         for j in range(col):
#             ele=float(input(f"Enter the element at pos {i+1},{j+1} : "))
#             r.append(ele)
#         res.append(r)
#     return res    
        
      
# row=int(input("ENter the number of rows: "))
# col=int(input("Enter the number of cols: "))

# def transpose(mat):
#     row=len(mat)
#     col=len(mat[0])
    
#     transp=[[0 for _ in range(row)]for _ in range(col)]
    
#     for i in range(row):
#         for j in range(col):
#             transp[j][i]=mat[i][j]
            
#     return transp


# mat1=get_input(row,col)

# for i in mat1:
#     print(i)
    
# print()    
    
# t=transpose(mat1)                
# for i in t:     
#          print(i)               
         
# def trace(mat) :
#     trace=0
    
#     if len(mat) == len(mat[0]):
#         for i in range(len(mat)):
#             trace+=mat[i][i] 
#         return trace

#     return "NOt a sqr matrix"

# print(trace(mat1))



    