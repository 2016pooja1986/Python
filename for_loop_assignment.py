data={}
l1=[1,2,3,4,5]
l2=["A","B","C","D","E"]

'''for i in range(len(l1)):
    data[i]=l2[i]

print(data)'''


#--------------------------OR-------------------------------

# 1


for i in range(6):
    print(i*'x')



# 2

for i in range(5,0,-1):
    print(i*'x')

# 3    
j=6
for i in range(6):
    j-=1
    print(j*' ',i*'x')
    


# 4

for i in range(6):
    print(5*'x')

# 5


for i in range(1,6):
    j=5
    for j in range(5,0,-1):
        print(i,end="")
    print("")

# 6

for i in range(1,6):
    j=1
  
    while j<=5:
        print(j,end="")
        j+=1
    print("")    

# 7

for i in range(1,6):
    j=i
    k=1
    while j>=1:
        print(k,end="")
        j-=1
        k+=1
    print("")    
# 8

for i in range(1,6):
    j=i
    while j>=1:
        print(i,end="")
        j-=1
        
    print("")

# 9


for i in range(1,6):
    j=i
    k=65
    while j>=1:
        print(chr(k),end="")
        j-=1
        k+=1
    print("")

# 10
k=65
for i in range(1,6):
    j=i   
    while j>=1:
        print(chr(k),end="")
        j-=1
    k+=1    
    print("")

# 11

k=12
for i in range(1,7):
    for j in range(k,0,-1):
        print(end=" ")
    k-=1
    for j in range(0, i ):
        print("*", end=" ")
    print("")    

# 12
k=7
for i in range(6,0,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k+=1
    for j in range(0, i ):
        print("*", end=" ")
    print("")
 
