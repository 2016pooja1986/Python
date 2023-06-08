#Q1. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :-   
#        Cost price (in Rs)                                Tax
#        > 100000                                          15 %
#        > 50000 and <= 100000                             10%
#        <= 50000                                           5%

tax = float(input("Enter the cost price of bike = Rs "))

if tax>100000:
    print("Road tax = Rs", 0.15*tax)
elif tax >50000 and tax<=100000:
    print("Road tax = Rs", 0.10*tax)
else:
    print("Road tax = Rs", 0.05*tax) 

#Q2. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on?

week = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
a = int(input("Enter the number from 1 to 7 ="))

if a<=7:
    print("The name of day is ",week[a])
else:
    print("Enter the number between 1 to 7 .")

#Q3. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on?

month = {1:'January',2:'Febraury',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
a = int(input("Enter the number from 1 to 12 ="))

if a<=12:
    print("The name of month is ",month[a],'and no of days are ',days[a])
else:
    print("Enter the number between 1 to 12 .")    

#Q4. Accept any city from the user and display monument of that city?
#                  City                                 Monument
#                  Delhi                               Red Fort
#                  Agra                                Taj Mahal
#                  Jaipur                              Jal Mahal

monu = {'Delhi':'Red Fort','Agra':'Taj Mahal','Jaipur':'Jal Mahal'}
city = input("Enter the name of city = ")
city = city.capitalize()

if city in monu:
    print("The name of monument in ",city," is ",monu[city])
else:
    print("No information for this city")
    
#Q5. Write a program to accept percentage and display the Category according to the  following criteria :-
#Percentage		Category
#< 40		Failed
#>=40 & <55	Fair
#>=55 & <65	Good
#>=65		Excellent

marks = float(input("Enter the obtained percentage(%) :"))

if marks < 40 :
        print("Failed ")
elif marks>=40 and marks<55:
        print("Fair")
elif marks>=55 and marks<65:
        print("Good")      
else :
        print("Excellent")
    


#Q6. Write a program to accept two numbers and mathematical operators (+,-,*,/,%,**,//,==) and perform operation accordingly?
#Like:Enter First Number: 7;Enter Second Number : 9 ;Enter operator : +;Your Answer is : 16

a = float(input("Enter the first number="))
b = float(input("Enter the second number="))

op= input("Enter the operator(+,-,*,/,**,%,//,= ):")

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
elif op == '//':
    print (" Quotient = ",a//b)       
else:
    print("Invalid operation")


#Q7. Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly:-
#Age		Sex	Wage/day
#>=18 and <30	 M/F	   700 /750 
#>=30 and <=40	 M/F	    800/850

age = int(input("Enter the age of person :  "))
sex = input("Enter the sex of person(M/F):  ")

if age>=18 and age<30 and sex.upper()=='M':
    print("The wage of person is = Rs 700")
elif  age>=18 and age<30 and sex.upper()=='F':   
     print("The wage of person is = Rs 750")
elif age>=30 and age<=40 and sex.upper()=='M':
    print("The wage of person is = Rs 800")
elif age>=30 and age<=40 and sex.upper()=='F':
    
    print("The wage of person is = Rs 850")
else:
    print("No wages")    
     
'''  OR
if age>=18 and age<30:
    if sex.upper()=='M':
        print("The wage of person is = Rs 700")
    elif  sex.upper()=='F':
        print("The wage of person is = Rs 750")  
          
elif age>=30 and age<=40:
    if sex.upper()=='M':
        print("The wage of person is = Rs 800")
    elif  sex.upper()=='F':
        print("The wage of person is = Rs 850")
else:
    print("No wages")'''

#Q8. Accept the electric units from user and calculate the bill according to the following rates:-
#First 100 Units     :  Free;Next 200 Units      :  Rs 2 per unit.;Above 300 Units    :  Rs 5 per unit.if number of unit is 500 then total bill = 0 +400 + 1000 = 1400
        
unit = int(input("Enter the no of unit consumed :"))

if unit <=100:
        charge = 0
elif (unit > 100 and unit <=300):
        charge = (unit-100)*2
else:
        charge = 200*2 + (unit -300)*5
print(" Total bill amount is Rs ",charge)


#Q9. Accept the number of days from the user and calculate the charge for library according to following :-
#Till five days   : Rs 2/day. Six to ten days  : Rs 3/day. 11 to 15 days : Rs 4/day After 15 days : Rs 5/day

days = int(input("Enter the no of days :"))

if days <=5:
        charge = 2*days
elif (days > 5 and days <=10):
        charge = days*3
elif (days > 10 and days <=15):
        charge = days*4
else:
        charge = days*5
print(" Total charge for library is Rs ",charge)


#Q10. Accept the kilometers covered and calculate the bill according to the following criteria:-
#First 10 Km             Rs11/km ; Next 90Km               Rs 10/km  ; After that              Rs9/km

dist = int(input("Enter the distance in km : "))

if dist <=10:
        charge = 11*dist
elif (dist > 10 and dist <=100):
        charge = 11*10 + 10*(dist -10)
else:
        charge = 11*10 + 10*90 + (dist -100)*9
print(" Total bill of cab is Rs ",charge)
