#Q1. Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye"?

num = float(input("Enter the number = "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

#Q2. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not?

num = float(input("Enter the number = "))

if num % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")   

#Q3. Write a program to check whether a number entered is three digit number or not?

num = int(input("Enter the number = "))

if num <1000 and num >99:
    print("Entered number is three digit number")
else:
    print("Entered number is not three digit number")      

#Q4. Write a program to check whether a person is senior citizen or not?

age = int ( input ( "Enter the age of the person: " ) )

if age >= 60:
    print ( " The person is Senior citizenship ")

else :
    print ( " The person is not Senior citizenship ")
 

#Q5. Write a program to check whether a number (accepted from user) is positive or negative?

num = int(input("Enter the number = "))

if num <0 :
    print("Entered number is negative")
else:
    print("Entered number is positive")     

#Q6. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both?

num = float(input("Enter the number = "))

if num % 3 == 0 and num % 2 ==0:
    print("Number is divisible by 2 and 3 both")
else:
    print("Number is not divisible by 2 and 3 both")  

#Q7. Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 degree C.

temp = int(input("Enter temperature in degree Celsius = "))

if temp >=100 :
    print("Water is boiling")
else:
    print("Water is not boiling")     

#Q8. Write a program to check a character is vowel or not?

v = ['a','e','i','o','u']

char = input("Enter the character : ")

if char in v:
    print(" A character is vowel")
else:
    print(" A character is not vowel")

#Q9. Accept the following from the user and calculate the percentage of class attended:-
#a.  Total number of working days?
#b.  Total number of days for absent?
#After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam?

total = int(input("Enter the total working days= "))
absent = int(input("Enter the no of absent days= "))

if (absent*100)/total >25:
    print("Student will not be able to sit in exam")
else:
    print("Student can sit in exam")


#Q10. Accept three sides of triangle and check whether the triangle is possible or not?(triangle is possible only when sum of any two sides is greater than 3rd side)

s1,s2,s3 = map(int,input("Enter 3 sides of triangle : ").split())

if s1+ s2 > s3 and s1 +s3 >s2 and s2 + s3 >s1:
    print("The triangle with sides",s1,",",s2,"and",s3," is possible")
else:
    print("The triangle with sides",s1,",",s2,"and",s3," is not possible")
