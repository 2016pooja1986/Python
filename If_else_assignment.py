
#1. Insurance program

status = input("Enter the status of employee (married/unmarried): ")


if status.lower() == 'married':
               print("Employee is eligible for insurance")
               
elif status.lower() == 'unmarried':
    
    gen = input("Enter the gender of employee:")
    if gen.lower() == 'male':
        age = int(input("Enter the age of employee:"))
        if age > 30:
                print("Employee is eligible for insurance")
        else :   
                print("Employee is not eligible for insurance")
                
    elif gen.lower() == 'female':
        age = int(input("Enter the age of employee:"))
        if age > 25:
                print("Employee is eligible for insurance")
        else :   
                print("Employee is not eligible for insurance")

else:
        print("Invalid status of employee")



# 2.Calculation Program

a = float(input("Enter the first number="))
b = float(input("Enter the second number="))

op= input("Enter the operator(+,-,*,/,**,% ):")

if op == '+':
    print (" Addition = ",a+b)
    
elif op == '-':
    print (" Subtraction = ",a-b)
elif op == '*':
    print (" multiplication = ",a*b)
elif op == '/':
    print (" division = ",a/b)
elif op == '**':
    print (a," raised to power ",b,"is ",a**b)
elif op == '%':
    print (" remainder = ",a%b)    
else:
    print("Invalid operation")


#3. checking of character
#A to Z =[65 to 90];a to z =[97 to 122];0 to 9=[48 to 57];special symbols=[0 to 47][58 to 64][91 to 96][123 to 127]

ch = input("Enter the character: ")
ch = ord(ch)
if ch>=65 and ch<=90:
    print("The character is in upper case")
if ch>=97 and ch<=122:
    print("The character is in lower case")
if ch>=48 and ch<=57:
    print("The character is digit")
if (ch>=0 and ch<=47) or  (ch>=58 and ch<=64) or (ch>=91 and ch<=96) or (ch>=123 and ch<=127) : 
    print("It is special character")
    
''' # -----------------OR----------------------------------------
a = input("Enter the character: ")

if a.islower() == True:
    print("The character is in lower case")
if a.isupper() ==True:
    print("The character is in upper case")
if  a.isdigit() == True:
    print("The character is digit")
if a.isalnum()==False:
    print("The character is special")'''

#4.TYPES OF TRIANGLE


s1,s2,s3 = map(int,input("Enter 3 sides of triangle : ").split())

if s1==s2 and s2==s3:
    print("It is equilateral triangle")
if s1==s2 or s1==s3 or s2==s3:
    print(" It is isoceles triangle")
if s1!=s2 and s1!=s3 and s2!=s3:
    print("It is scelene triangle")

#5.Even and odd number

num = int(input("Enter the number = "))

if num % 2 ==0:
    print("It is even number")
else:
    print("It is odd number")

#6. leap year

yr = int(input("Enter the year = "))

if yr% 4==0:
    print("It is leap year")
else:
    print("It is not leap year")

#7.reverse case
#A to Z =[65 to 90];a to z =[97 to 122];0 to 9=[48 to 57];special symbols=[0 to 47][58 to 64][91 to 96][123 to 127]

ch = input("Enter the character: ")
ch = ord(ch)
if ch>=65 and ch<=90:
    ch = ch+32
    print(chr(ch))
if ch>=97 and ch<=122:
    ch = ch-32
    print(chr(ch))


'''
-----------------OR---------------
char = input("Enter the character :")

if char.islower()== True:
    print(char.upper())
else:    
    print(char.lower())'''

#8. Basic salary

sal = float(input("Enter the basic salary of an employee:"))
NET_SALARY = 0.00
if sal>10000:
    DA = 0.1*sal
    HRA = 0.2*sal
    TA = 0.05*sal
    NET_SALARY = sal + DA + HRA + TA
    print("DA = Rs ",DA,"\nHRA = Rs",HRA,"\nTA = Rs",TA,"\nNET SALARY = Rs",NET_SALARY)

else:
     print("NO DA,HRA and TA .\nNET SALARY = Rs",NET_SALARY=sal)

#9. largest number among 3 numbers without using nested if and logical operator

a,b,c= map(int,input("Enter the values of 3 numbers : ").split(','))

d =a
if b >a:
   d=b
if c> b:
   d =c
print("Largest   no is ",d)                    

    

    
    

    

        
        
