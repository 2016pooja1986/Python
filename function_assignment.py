
print("\n \n Question 1:2 arguments no return value")
def odd(a,b):
    'print all odd no between 1 to 100'
    print("\n Total odd no from ",a," to ",b, " = ",[x for x in range(a,b) if x%2 !=0 ])
   

odd(1,100)



print("\n \n Question 2:2 arguments no return value")
def even(a,b):
    'print all even no between 1 to 100'
    print("\n Total even no from ",a," to ",b, " = ",[x for x in range(a,b) if x%2 ==0 ])
   

even(1,100)


print("\n \n Question 3 : 1 argument no return value")

def table(n):
    'Table of any given no'
    for i in range(1,11):
        print(n,"*",i,"= ",n*i)

n = int(input("Enter the number= "))
table(n)



print("\n \n Question 4: 1 argument 2 return values")
def fact(n):
    'factorial of number'
    f=1
    s=n
    st=''
    for i in range(n,0,-1):
        f*=i
        if s==1:
            st += str(s)
        else:
            st += str(s)+'*'
        s-=1
    return st,f
    
n = int(input("Enter the number= "))
st,f=fact(n)
print("Factorial of ",n,"= ",st,"=",f)




print("\n \n Question 5: No argument no return")

def fibo():
    'Fibonacci series'
    n1, n2 = 0, 1   # first two terms
    n = int(input("Enter no of terms= "))
    if n == 1:
       print("Fibonacci sequence upto",n,":")
       print(n1)

    else:
       print("Fibonacci sequence:")
       for i in range(0, n):
           print(n1, end=" ")
           nth = n1 + n2
           n1 = n2
           n2 = nth
fibo()    



print("\n \n Question 6: No argument 1 return value")

def prime():
    'prime and composite number'
    global n
    n = int(input("Enter the number= "))
    factor=0
    for i in range(1,n+1):
        if n%i==0:
            factor +=1
    return factor
f=prime()
if f==2:
    print(n," is the prime number")
elif f==1:
    print(n," is the neither prime nor composite number")
else:
     print(n," is the composite number")



     
