#1. print all odd no between 1 to 100
i=3
count=0
while i<100:
    print(i,end=" ")
    i+=2
    count+=1
print("\n Total odd no between 0 to 100 = ",count)

#-------------------------OR-------------------------
print("\n \n Solution using LC")
print("\n Total odd no between 0 to 100 = ",[ i for i in range(3,100) if i%2!=0])


#2. print all even no between 1 to 100
print("\n \n Question 2")
i=2
count=0
while i<100: 
    print(i,end=" ")
    i+=2
    count+=1
print("\n Total even no between 0 to 100 = ",count)

#-------------------------OR-------------------------
print("\n \n Solution using LC")
print("\n Total even no between 0 to 100 = ",[ i for i in range(2,100) if i%2==0])

#3. Table of any given no
print("\n \n Question 3")
n = int(input("Enter the number= "))

i=1

while i<=10:
    print(n,"*",i,"= ",n*i)
    i+=1
#-------------------------OR-------------------------
print("\n \n Solution using LC")
print([n*i for i in range(1,11)])

#4.factorial of number

n = int(input("Enter the number= "))
i=n
fact=1
s=n
st=''

while i>=1:
    fact*=i
    i-=1
    if s==1:
        st += str(s)
    else:
        st += str(s)+'*'
    s-=1
    
print("Factorial of ",n,"= ",st,"=",fact)

#-------------------------OR-------------------------
print("\n \n Solution using LC")
import math as m
print([m.factorial(i) for i in range(1,11)])

#5.Fibonacci series

n = int(input("Enter no of terms= "))
          
n1, n2 = 0, 1   # first two terms
count = 0

if n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#6. prime and composite number

n = int(input("Enter the number= "))

i=1
factor=0
while i<=n:
    if n%i==0:
        factor +=1
    i+=1
if factor ==2:
    print(n," is the prime number")
elif factor ==1:
     print(n," is the nor prime and composite number")
else:
    print(n," is the composite number")     



     
