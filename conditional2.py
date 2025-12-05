#1
# a=int(input('enter a number:'))
# b=int(input('enter another number:'))
# c=int(input('enter a number:'))
# if a>b and a>c:
#     print('a is largest')
# elif b>a and b>c:
#     print('b is largest')
# else:
#     print('c is largest')

#------1
#2
# month=int(input('enter a month number:'))
# if month==1:
#     print('the month is january')
# elif month==2:
#     print('the month is february:')
# elif month==3:
#     print('the month is march')
# elif month==4:
#     print('the month is april')
# elif month==5:
#     print('the month is may')
# elif month==6:
#     print('the month is june')
# elif month==7:
#     print('the month is july')
# elif month==8:
#     print('the month is august')
# elif month==9:
#     print('the month is september')
# elif month==10:
#     print('the month is october')
# elif month==11:
#     print('the month is november')
# elif month==12:
#     print('the month is december')
# else:
#     print('invalid number')

#--------2
#3
# a=int(input('enter a variable:'))
# b=int(input('enter another variable:'))
# temp=a
# a=b
# b=temp
# print(a,b)

#-----3
#3
# a=int(input('enter a variable:'))
# b=int(input('enter another variable:'))
# a,b=b,a
# print(a,b)

#------3
#4
# age=int(input('enter your age:'))
# if age<12:
#     print('the ticket is free')
# elif age>=12 and age<=60:
#     membership_card=input('do the person have mebership card?:')
#     if membership_card=='yes':
#         price=150
#         print(price)
#     else:
#         price=200
#         print(price)
# else:
#     price=100
#     print(price)

#-----4
#5
# units = int(input("Enter electricity usage in units: "))

# if units < 100:
#     cost = units * 5

# elif units <= 300:
#     cost = (100 * 5) + (units - 100) * 8

# else:
#     cost = (100 * 5) + (200 * 8) + (units - 300) * 10

# print("Total bill = Rs", cost)

#-------5
#6
# p1=input('enter your move: rock, paper, scissors:')
# p2=input('enter your move: rock, paper, scissors:')
# if p1=='rock':
#     if p2=='rock':
#         print('tie')
# elif p1=='scissors':
#     if p2=='scissors':
#         print('tie')
# elif p1=='paper':
#     if p2=='paper':
#         print('tie')
# elif p1=='rock':
#     if p2=='paper':
#      print('p2 wins')
#     else:
#         print('p1 wins')
# elif p1=='scissors':
#     if p2=='paper':
#         print('p1 wins')
#     else:
#         print('p2 wins')
# elif p1=='rock':
#     if p2=='scissors':
#         print('p1 wins')
#     else:
#         print('p2 wins')
    
#------
#7
# Input number of students
# a = int(input("Enter number of students in class A: "))
# b = int(input("Enter number of students in class B: "))
# c = int(input("Enter number of students in class C: "))
# if  a%2==0:
#     desks_a = a // 2
# else:
#     desks_a = a // 2 + 1   # 
# if b % 2 == 0:
#     desks_b = b // 2
# else:
#     desks_b = b // 2 + 1
# if c % 2 == 0:
#     desks_c = c // 2
# else:
#     desks_c = c // 2 + 1
# total_desks = desks_a + desks_b + desks_c
# print("Minimum number of desks required =", total_desks)

#______
#8
# current_floor=5
# person_floor=int(input('enter the floor number you want to go:'))
# if person_floor==current_floor:
#     print('lift stays on same floor')
# else:
#   if person_floor>current_floor:
#     print('lift goes up')
#   else:
#     print('lift goes down')


# -----
#9
# a=int(input('enter a number:'))
# if a>0:
#     print('positive')
#     if a%2==0:
#         print('even')
#     else:
#         print('odd')
# elif a==0:
#     print('zero')
# else:
#     print('negative')

#_______
#10
# a=int(input('enter a number:'))
# b=int(input('enter another number:'))
# if a>b:
#     print('a is greater')
# elif a==b:
#     print('both are equal')
#     if (a==b)>0:
#         print('positive')
#     if (a==b)<0:
#         print('negative')
#     if (a==b)==0:
#         print('zero')
# else:
#     print('b is greater')

#------
#11
# num1=int(input('enter a number:'))
# if num1%3==0 and num1%5==0 :
#     print('fizz buzz')
# elif num1%3==0 and num1%5!=0:
#     print('fizz')
# elif num1%3!=0 and num1%5==0:
#     print('buzz')
# else:
#     print('number')

#-----
#12
# import random
# num=random.randint(0,5)
# if num==0:
#     print('Flamingos turn pink from eating shrimp.')
# elif num==1:
#     print("The only food that doesn't spoil is honey")
# elif num==2:
#       print("Shrimp can only swim backwards.")
# elif num == 3:
#     print("A taste bud's life span is about 10 days.")
# elif num == 4:
#     print("A snail can sleep for three years.")
# else:
#     print("Bananas are berries, but strawberries aren't.")

#-----
#13
# total_amount = float(input("Enter total purchase amount: "))
# is_member = input("Is the customer a member? (True/False): ")
# is_member = is_member == "True"

# if total_amount > 1000 and is_member:
#     final_amount = total_amount - (total_amount * 0.20)
# elif total_amount > 1000 and not is_member:
#     final_amount = total_amount - (total_amount * 0.10)
# else:
#     final_amount = total_amount

# print("Final amount to pay:", final_amount)
#14
# earth_weight = float(input("Enter your weight on Earth: "))
# planet = int(input("Enter planet number (1-7): "))

# if planet == 1:
#     final_weight = earth_weight * 0.38
# elif planet == 2:
#     final_weight = earth_weight * 0.91
# elif planet == 3:
#     final_weight = earth_weight * 0.38
# elif planet == 4:
#     final_weight = earth_weight * 2.53
# elif planet == 5:
#     final_weight = earth_weight * 1.07
# elif planet == 6:
#     final_weight = earth_weight * 0.89
# elif planet == 7:
#     final_weight = earth_weight * 1.14
# else:
#     final_weight = None

# if final_weight is not None:
#     print("Your weight on that planet is:", final_weight)
# else:
#     print("Invalid planet number")

#15
# m1 = float(input("Enter marks of subject 1: "))
# m2 = float(input("Enter marks of subject 2: "))
# m3 = float(input("Enter marks of subject 3: "))
# m4 = float(input("Enter marks of subject 4: "))

# total = m1 + m2 + m3 + m4
# percentage = (total / 400) * 100

# if percentage > 70:
#     grade = "Distinction"
# elif percentage > 60:
#     grade = "First"
# elif percentage > 40:
#     grade = "Pass"
# else:
#     grade = "Fail"

# print("Total Marks:", total)
# print("Percentage:", percentage, "%")
# print("Grade:", grade)

#16
# cost = float(input("Enter the cost price of the bike: "))

# if cost > 100000:
#     tax = cost * 0.15
# elif cost > 50000 and cost <= 100000:
#     tax = cost * 0.10
# else:
#     tax = cost * 0.05

# print("Road tax to be paid:", tax)

#17
# years = float(input("Enter years of service: "))

# if years > 10:
#     bonus = 0.10
# elif years >= 6 and years <= 10:
#     bonus = 0.08
# else:
#     bonus = 0.05

# print("Bonus percentage:", bonus * 100, "%")

#18
# score = float(input("Enter subject score: "))

# if score > 90:
#     print("Congratulations!")
# elif score >= 50 and score <= 90:
#     print("You can improve.")
# else:
#     print("Consider retaking the course.")

# #19
# age = int(input("Enter your age: "))

# if age >= 18:
#     degree = input("Do you have a degree? (yes/no): ")
#     if degree == "yes":
#         experience = float(input("Enter years of experience: "))
#         if experience > 3:
#             print("Highly Eligible")
#         elif experience >= 1:
#             print("Eligible")
#         else:
#             print("Under Review")
#     else:
#         print("Not Eligible (No degree)")
# else:
#     print("Not Eligible (Age below requirement)")

# #20
# age = int(input("Enter age: "))
# gender = input("Enter gender (M/F): ")
# days = int(input("Enter number of days worked: "))

# if age >= 18 and age < 30:
#     if gender == "M":
#         wage = 700
#     else:
#         wage = 750
# elif age >= 30 and age <= 40:
#     if gender == "M":
#         wage = 800
#     else:
#         wage = 850
# else:
#     wage = 0

# if wage > 0:
#     print("Total wages:", wage * days)
# else:
#     print("Not eligible for wage")

# #21
# is_valid = True
# balance = 50000
# pin = int(input("Enter PIN: "))

# if is_valid:
#     if pin == 123:
#         print("1. Withdraw")
#         print("2. Check Balance")
#         print("3. Exit")
#         option = int(input("Enter option: "))

#         if option == 1:
#             amount = int(input("Enter amount to withdraw: "))
#             if amount <= balance:
#                 balance -= amount
#                 print("Withdrawal successful. Remaining balance:", balance)
#             else:
#                 print("Insufficient balance")
#         elif option == 2:
#             print("Current balance:", balance)
#         elif option == 3:
#             print("Thank you for visiting")
#         else:
#             print("Invalid option")
#     else:
#         print("Wrong PIN")
# else:
#     print("Invalid Card")

# #22
# print("Welcome to the Magic Forest")
# direction = input("Do you want to go north or south? ")

# if direction == "south":
#     print("Game Over")
# elif direction == "north":
#     choice = input("Do you want to cross the river or follow the path? ")
#     if choice == "cross the river":
#         print("Game Over")
#     elif choice == "follow the path":
#         creature = input("Choose fairy, ogre or elf: ")
#         if creature == "elf":
#             print("You Win")
#         else:
#             print("Game Over")
#     else:
#         print("Invalid choice")
# else:
#     print("Invalid direction")

# #23
# print("Welcome to the Haunted House")
# direction = input("Do you want to go upstairs or downstairs? ")

# if direction == "downstairs":
#     print("Game Over")
# elif direction == "upstairs":
#     choice = input("Do you want to enter the room or stay outside? ")
#     if choice == "enter the room":
#         print("Game Over")
#     elif choice == "stay outside":
#         creature = input("Choose ghost, vampire or werewolf: ")
#         if creature == "werewolf":
#             print("You Win")
#         else:
#             print("Game Over")
#     else:
#         print("Invalid choice")
# else:
#     print("Invalid direction")



