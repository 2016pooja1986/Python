#Q1. Write a program to calculate the electricity bill using only if statement ?(accept number of unit from user) according to the following criteria :-
#      Unit                                                     Price  
#First 100 units                                               no charge
#Next 100 units                                              Rs 5 per unit
#After 200 units                                             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)


unit = int(input("Enter the no of unit consumed :"))

if unit <=100:
        charge = 0
if (unit > 100 and unit <=200):
        charge = (unit-100)*5
if unit > 200:
        charge = 100*5 + (unit -200)*10
print(" Total bill amount is Rs ",charge)


#Q2. Write a program to accept percentage from the user and display the grade according to the following criteria:-
#        Marks                                    Grade
#         > 90                                      A
#        > 80 and <= 90                             B
#         >= 60 and <= 80                           C
#         below 60                                  D


marks = float(input("Enter the obtained marks :"))

if marks > 90 :
        print(" Scored grade A ")
if marks>80 and marks<=90:
        print("Scored grage B")
if marks>=60 and marks<=80:
        print("Scored grade C")      
if marks<60:
        print("Scored grade D")


#Q3. Accept the age of 4 people and display the youngest one?

p1,p2,p3,p4 = map(int,input("Enter the age of 4 people :").split(","))

if p1 < p2:
        if p1 < p3:
                if p1 <p4:
                        print(" 1st person of age ", p1,"yrs is youngest. ")
                else:
                        print(" 4th person of age ", p4,"yrs is youngest. ")
        elif p3<p4:
                 print(" 3rd person of age ", p3,"yrs is youngest. ")
        else:
                 print(" 4th person of age ", p4,"yrs is youngest. ")
elif p2<p3:
        if p2 < p4:
                print("2nd person of age ", p2,"yrs is youngest. ")
        else:
                print(" 4th person of age ", p4,"yrs is youngest. ")

else:
        if p3<p4:
            print(" 3rd person of age ", p3,"yrs is youngest. ")
        else:
            print(" 4th person of age ", p4,"yrs is youngest. ")

#Q4. A company decided to give bonus to employee according to following criteria:-
#    Time period of Service                Bonus
#    More than 10 years                     10%
#    >=6 and <=10                           8%
#    Less than 6 years                      5%
#Ask user for their salary and years of service and print the net bonus amount?

sal = float(input("Enter the salary of employee: Rs"))
yrs = float(input("Enter the years of service : "))

if yrs > 10:
    print("Net bonus amount is Rs", 0.1 * sal)
if yrs >=6 and yrs<=10:
    print("Net bonus amount is Rs", 0.08 * sal)
if yrs <6:
    print("Net bonus amount is Rs", 0.05 * sal)


#Q5. Accept three numbers from the user and display the second largest number?

a,b,c =map(int,input("Enter the values of three numbers :").split(","))

if a>b and a<c:
    print(a," is the 2nd largest no.")
if b>a and b<c:
    print(b," is the 2nd largest no.")
if c>a and c<b:
    print(c," is the 2nd largest no.")    


#Q6. Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) to pay according to following criteria:-
#Marked Price	                 Discount
#   >10000	                         20%
#   >7000 and <=10000	              15%
#   <=7000	                         10%


mp = float(input("Enter the marked price of item = Rs "))

if mp > 10000:
    print("Net amount is Rs",mp- 0.2 * mp)
if mp >7000 and mp<=10000:
    print("Net amount is Rs",mp- 0.15 * mp)
if mp <= 7000:
    print("Net amount is Rs",mp- 0.1 * mp)


#Q7. Accept the marks of English, Math and Science, Social Studies Subject and display the stream allotted according to following:-
#All Subjects more than 80 marks      —         Science Stream
#English >80 and Math, Science above 50   —    Commerce Stream
#English > 80 and Social studies > 80    —      Humanities

eng =float(input("Enter the English marks = "))
math =float(input("Enter the Math marks = "))
sci = float(input("Enter the Science marks = "))
sst =float(input("Enter the Social Studies marks = "))

if eng>80 and math>80 and sci >80 and sst >80:
    print("Student has got Science Stream")
if eng>80 and math>50 and sci >50 :
    print("Student has got Commerce Stream")
if eng>80 and sst >80:
    print("Student has got Humanities")    
    

    
            


                
