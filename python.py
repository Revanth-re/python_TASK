# # problems on using if and elif
# #1.Program to check if a number is positive, negative, or zero
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is a positive number.") 
# elif num < 0:
#     print(f"{num} is a negative number.")
# else:
#     print("The number is zero.")
# #---*----*-----*  
# # 2.Determine if a number is odd or even.     
# num = int(input("Enter a number: "))
# if num%2==0:
#     print(f"{num} is a even")
# elif num%2==1:
#     print(f"{num} is a odd")

# #---*----*-----*    
# # 3. Check if a person is eligible to vote (age >= 18).  
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote!")
# else:
#     print("You are not eligible to vote yet.")
# #---*----*-----*    
# # 4.write a Program to find the greatest of two numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if num1 > num2:
#     print("The greatest number is",{num1})
# elif num2 > num1:
#     print("The greatest number is",{num2})
# else:
#     print("Both numbers are equal.")
# #---*----*-----*    
# #5. Print "Pass" if a student scores more than 40 marks;  otherwise, print "Fail." 
# marks = int(input("Enter the student's marks: "))
# if marks > 40:
#     print("Pass")
# else:
#     print("Fail")
# #---------------------------------------------------------------------------
# #6.Write a program to display the day of the week based on a  number input (1 for Monday, 2 for Tuesday, etc.). 
# num=int(input("Enter a number: "))
# if(num==1):
#     print("Monday")
# elif(num==2):
#     print("Tuesday")
# elif(num==3):
#     print("Wednesday")
# elif(num==4):
#     print("Thursday")
# elif(num==5):
#     print("Friday")
# elif(num==6):
#     print("saturday")
# elif(num==7):
#     print("Sunday") 
# else:
#     print("please enter from 1-7")          
# #---*----*-----*    
# #7.Implement a simple calculator to perform addition,  subtraction, multiplication, and division. 
# num1=int(input("Enter a number: "))          
# num2=int(input("Enter a number: ")) 
# num= input("enter operator").lower#to convert higher to lower   
# if(num == "add" or num== "+"):
#     print(num1+num2)    
# elif(num == "sub" or num == "-"):
#     print(num1-num2)   
# elif(num == "mul" or num == "*"):
#     print(num1*num2)    
# elif(num == "div" or num == "%"):  
#     print( num1 % num2)
# else:
#     print("invalid input") 
# #---------------------------------------------------------------------------------------------
# #8.Write a program to display the name of a month based on  the month number (1 for January, 2 for February, etc.). 
# num=int(input("Enter a number: "))
# if(num==1):
#     print("january")
# elif(num==2):
#     print("february")
# elif(num==3):
#     print("march")
# elif(num==4):
#     print("april")
# elif(num==5):
#     print("may")
# elif(num==6):
#     print("june")
# elif(num==7):
#     print("july")
# elif(num==8):
#     print("august")
# elif(num==9):
#     print("september")
# elif(num==10):
#     print("october")
# elif(num==11):
#     print("november")
# elif(num==12):
#     print("december")
# else:
#     print(" Please Enter from 1-12")

# #---*----*-----*    
# #medium qns:
# #1 write a program to find the greatest of three numbers  
# num1=int(input("Enter First number"))
# num2=int(input("Enter Second number"))
# num3=int(input("Enter Third number"))
# if (num1>num2):
#     print("The Greatest number is: ",{num1})
# elif(num1>num3):
#     print("The Greatest number is: ",{num1})
# elif(num2>num1):
#     print("The Greatest number is: ",{num2}) 
# elif(num2>num3):
#     print("The Greatest number is: ",{num2})
# elif(num3>num1):
#     print("The Greatest number is: ",{num3})
# elif(num3>num2):
#     print("The Greatest number is: ",{num3})
# else:
#     print("both are same") 
# #---*----*-----*    
# #2.check if a year is a leep years
# year=int(input("Enter a year: "))   
# if(year%4==0 & year%100!=0):
#     print("it is a leep year")  
# elif year%400==0:
#     print("it is a leep year")   
# else:
#     print("not a leep year")
# #---*----*-----*    
# #3.Write a program to classify a character entered by the user  as a vowel, consonant, or neither. 
# inp=input("enter an alphabit: ").lower()
# if len(inp)==1:
#     if inp.isalpha():
#       if inp in ["a","e","i","o","u"]:
#           print("vowels")
#       else:
#          print("consonants")
#     else:
#         print("special characters")
# else:
#     print("input is invalid") 
# #---*----*-----*    
# #4.Calculate the grade of a student based on the marks they  score: 
# # i.	90-100  : Grade A 
# # ii.	80-89  : Grade B 
# # iii.	70-79  : Grade C 
# # iv.	<70  : Fail. 

# marks=int(input("Enter your marks: "))
# if(marks>=90):
#     print("grade-A: ")
# elif(marks>=80):
#     print("grade-B: ")
# elif(marks>=70):
#     print("grade-C")
# elif(marks<70):
#     print("fail") 
# #---*----*-----*    
# #5.Write a program to check if three sides length form a valid  triangle. 
# side1=int(input("Enter first side1: "))       
# side2=int(input("Enter second side2: "))       
# side3=int(input("Enter third side3: ")) 
# if(side1 + side2 > side3  and side1 + side3 > side2 and side3 + side2 > side1):
#     print(" can form a triangle")     
# else:
#     print("cannot form a triangle")
# #---*----*-----*    
# #calaculating of fizz,buzz,and fizzbuzz :- 
# input=int(input("Enter a number: "))
# if(input%15==0):
#     print("fizzbuzz")
# elif(input%5==0):
#     print("buzz")
# elif(input%3==0):
#     print("fizz")  
# else:
#     print("invalid input")
# # ---------------------------------------------------------------------------------------------------------------
# #loops problems
# #1.	Print all numbers from 1 to 100 using a  for  loop. 

# for i in range(1,101):
#     print(i)
# #-------------------------------------------------------------------------------------------------------------------    
# #2.	Write a program to print the sum of the first  n  natural  numbers. (n*n+1/ 2)     
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum) 
# #-------------------------------------------------------------------------------------------------------------------    
# #3.	Print all even numbers between 1 and 50 using a  while  loop.
# num=0
# while num<51:
#     num+=1
#     if num%2==0:
#         print(num)
# #-------------------------------------------------------------------------------------------------------------------    
# #4.	Write a program to display the multiplication table of a given  number. First 20     
# for i in range(1,21):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
#     print("------------")    
# #-------------------------------------------------------------------------------------------------------------------    
# #5.	Reverse a number using a while  loop
# num=int(input("enter a number: "))
# sum=0
# while num>0:
#     sum+=num
#     print(num)
#     num-=1
# print(sum)  
# #-------------------------------------------------------------------------------------------------------------------    
# #6 Write a program to count the number of digits in a given  number using a  while  loop. 
# num=input("enter a number: ")
# while num:
#     print(str(len(num)))
#     break 
# #---------------------------------------------------------------------------------------------------------------------
# #divisble by 3 of given numbers,sum of given numbers,reverse of given numbers,and count
# num1 = 54312693
# sum=0
# rev=0
# count=0
# while num1 > 0:
#     rem = num1 % 10
#     sum+=rem
#     if rem%3==0:
#         print(rem)
#     rev=rev*10+rem
#     num1 = num1 // 10
#     count+=1
# print(rev)
# print(sum)
# print("count",count)
# #medium lopps
# # 4.Print all numbers from 1 to 100 that are divisible by 3 and 5  using a  for  loop. 
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)


# Implement a menu-driven program where the user can
# choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit.

#user_inp=input("enter the choice cube o square or exit:").lower()
# data=["square","cube","exit"]
# while True:
#     if(user_inp==data[2]):
#         print("you have successfully exited")
#         break
#     elif(user_inp==data[0]):
#         num=int(input("enter the number:"))
#         print(num**2)
#         user_inp=input("enter the choice cube o square or exit:").lower()
#     elif(user_inp==data[1]):
#         num=int(input("enter the number:"))
#         print(num**3)
#         user_inp=input("enter the choice cube o square or exit:").lower()
#     else:
#         print("please enter a valid name")
#         user_inp=input("enter the choice cube o square or exit:").lower()


