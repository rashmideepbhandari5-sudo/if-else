# Take 3 numbers and print the largest number

num1 = int(input('enter the number1: '))
num2 = int(input('enter the number2: '))
num3 = int(input('enter the number3: '))
if num1>num2>num3:
    print('num1 is greater than num2 and num3')
elif num2>num1>num3:
    print('num2 is greater than num1 and num3')
else:
    print('num3 is greater than num1 and num2')


# Take a month number (1–12) and print the month nam
num1=int(input('enter the num1: '))
if num1==1:
    print('jan')
elif num1==2:
    print('feb')
elif num1==3:
    print('mar')
elif num1==4:
    print('apr')
elif num1==5:
    print('may')
elif num1==6:
    print('jun')
elif num1==7:
    print('jul')
elif num1==8:
    print('aug')
elif num1==9:
    print('sep')
elif num1==10:
    print('oct')
elif num1==11:
    print('nov')
elif num1==12:
    print('dec')    
else:
    print('invalid')

# Write a program to swap two variables
# num1=int(input('enter the num1: '))
# num2=int(input('enter the num2: '))
# num1,num2=num2,num1
# print(num1)
# print(num2)

# # You are developing a simple ticket booking system for a movie theatre. The ticket
# price depends on the age of the person and whether they have a membership card. If
# the person is under 12, the ticket is free. If the person is between 12 and 60: if they
# have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs 200. If the
# person is above 60, they get a senior citizen discount, and then ticket costs Rs 100.
# Write a python program using nested if-else to calculate and print the ticket price
# based on the users age and membership status. 

age = int(input('enter the age: '))
if age < 12:
    print('ticket price is free')

elif age >= 12 and age <= 60:
    membership = input('enter the membership (yes/no): ')
    if membership == 'yes':
        print('ticket price is 150')
    else:
        print('ticket price is 200')
else:    # age > 60
     print('ticket price is 100')

     print('because the person is senior citizen')
  



# Write a complete Python program that:
#  Asks Player 1 to enter their move ( input: rock, paper, or scissors)
#  Asks Player 2 to enter their move ( input: rock, paper, or scissors)
#  Uses only nested if and else statements
#  Prints who wins or if it's a tie

player1=input('enter the player1: ')
player2=input('enter the player2: ')
if player1=='rock' and player2=='paper':
    print('player2 wins')
elif player1=='paper' and player2=='scissors':
    print('player2 wins')
elif player1=='scissors' and player2=='rock':
    print('player2 wins')
elif player1=='rock' and player2=='scissors':
    print('player1 wins')
elif player1=='paper' and player2=='rock':
    print('player1 wins')
elif player1=='scissors' and player2=='paper':
    print('player1 wins')
else:
    print('tie')



# A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
#  Next units: Rs 8
# If usage is > 300 units:
#  First 100: Rs 5
#  Next 200: Rs 8
#  Remaining: Rs 10

usage=int(input('enter the usage: '))
if usage<100:
    print('cost is 5 per unit')
elif usage<=300:
    print('first 100: Rs 5')
    print('next units: Rs 8')
else:
        print('first 100: Rs 5')
        print('next 200: Rs 8')
        print('remaining: Rs 10 ')


#   A school decided to replace the desks in three classrooms. Each desk sits two
# students. Given the number of students in each class, print the smallest possible
# number of desks that can be purchased. The program should read three integers: the
# number of students in each of the three classes, a, b and c respectively.
# 
# Hint: In the first test there are three groups. The first group has 20 students and thus
# needs 10 desks. The second group has 21 students, so they can get by with no fewer
# than 11 desks. 11 desks are also enough for the third group of 22 students. So, we
# need 32 desks in total

a=int(input('enter the A : '))
b=int(input('enter the B:'))
c=int(input('enter the C:'))

a=(a+1)//2
b=(b+1)//2
c=(c+1)//2
total=a+b+c
print(total)

#  In a smart building lift system, the lift is currently at floor 5. A person presses
# floor 3. Write a program to decide and display whether the lift should go up, go
# down, or stay at current floor.

# Write a Python program that takes a number as input, first checks if it is positive
# if yes then check whether it is even or odd

num=int(input('enter the number:'))
if num>0:
    print("positive number")
elif num<0:
    print('negative number')
else:
    print("zero")


# Take two numbers and find the greater of the two. If they are equal, check if the
# number is positive, negative, or zero


num1=int(input('enter the num1:'))
num2=int(input('enter the num2:'))
if num1>num2:
    print('num1 is greater than num2')
elif num1<num2:
    print('num1 is smaller than num2')
else:
    print('num1 is equal to num2')
    if num1>0:
        print('num1 is positive')
    elif num1<0:
        print('num1 is negative')
    else:
        print('num1 is zero')


# Accept input from user If given number is a multiple of both 3 and 5 prints "Fizz
# Buzz" instead of number If given number is a multiple of 3 but not 5 prints "Fizz"
# instead of number If given number is a multiple of 5 but not 3 prints "Buzz"instead
# of number If given number is not multiple of 3 or 5 prints value as usual.

num=int(input('enter the number:'))
if num%3==0 and num%5==0:
    print('fizz buzz')
elif num%3==0 or num%5!=0:
    print('fizz')
elif num%5==0 and num%3!=0:
    print('buzz')
else:
    print('invalid')



# . Snapple is a famous tea drink brand from Queens, New York. Each bottle cap
# comes with a silly fun fact.
# Use the random module to create a number from 0 to 5. Then use
# an if/elif/else statement to print out one of these six random Snapple facts:
# 0 - 'Flamingos turn pink from eating shrimp.'
# 1 - 'The only food that doesn't spoil is honey.'
# 2 - 'Shrimp can only swim backwards.'
# 3 - 'A taste bud's life span is about 10 days.'
# 4 - 'It is impossible to sneeze while sleeping.'
# 5 - 'It is illegal to sing off-key in North Carolina.'

import random
num=random.randint(0,5)
if num==0:
    print('Flamingos turn pink from eating shrimp.')
elif num==1:
    print('The only food that doesn\'t spoil is honey.')
elif num==2:
    print('Shrimp can only swim backwards.')
elif num==3:
    print('A taste bud\'s life span is about 10 days.')
elif num==4:
    print('It is impossible to sneeze while sleeping.')
elif num==5:
    print('It is illegal to sing off-key in North Carolina.')
else:
    print('invalid')


# A store gives a 20% discount if the total purchase is above RS 1000 AND the
# customer is a member, or a 10% discount if the purchase is above RS 1000 but the
# customer is not a member. Write a program that takes total_amount and
# is_member (True/False) as input and prints the final amount after applying the
# correct discount (or no discount).



total_amount = float(input('Enter the total amount: '))
is_member = input('Are you a member? (yes/no): ')
if total_amount > 1000 and is_member == 'yes':
    discount = 0.20
elif total_amount > 1000 and is_member == 'no':
    discount = 0.10
else:
    discount = 0.0
final_amount = total_amount * (1 - discount)
print(f"Discount applied: {discount*100}%")
print(f"Final amount to pay: RS {final_amount:.2f}")


# 14)

earth_weight = float(input("Enter your weight on Earth (kg): "))
planet_number = int(input("Enter planet number (1-Mercury, 2-Venus, 3-Mars, 4-Jupiter, 5-Saturn, 6-Uranus, 7-Neptune): "))
if planet_number == 1:
    destination_weight = earth_weight * 0.38
    planet_name = "Mercury"
elif planet_number == 2:
    destination_weight = earth_weight * 0.91
    planet_name = "Venus"
elif planet_number == 3:
    destination_weight = earth_weight * 0.38
    planet_name = "Mars"
elif planet_number == 4:
    destination_weight = earth_weight * 2.53
    planet_name = "Jupiter"
elif planet_number == 5:
    destination_weight = earth_weight * 1.07
    planet_name = "Saturn"
elif planet_number == 6:
    destination_weight = earth_weight * 0.89
    planet_name = "Uranus"
elif planet_number == 7:
    destination_weight = earth_weight * 1.14
    planet_name = "Neptune"
else:
    print("Invalid planet number!")
    destination_weight = None
if destination_weight is not None:
    print(f"Your weight on {planet_name} would be: {destination_weight:.2f} kg")


#  WAP which accepts marks of four subjects and display total marks, percentage and
# grade. Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –>
# pass, less than 40 –> fail

mark1=int(input('enter the mark:'))
mark2=int(input('enter the mark2:'))
mark3=int(input('enterthe mark3:'))
mark4=int(input('enter the mark4:'))
total_mark=mark1+mark2+mark3+mark4
print(total_mark)
percentage=(total_mark/4)
print(percentage)
if percentage>=70:
    print("distinction")
elif percentage<70 and percentage>=60:
    print('first division')
elif percentage<60 and percentage>=40:
    print('pass')
else:
    print('fail')

# Write a program to accept the cost price of a bike and display the road tax to be
# paid according to the following criteria:
# Cost price (in Rs)      Tax
# >100000                15%
# >50000 and  <=100000    10%
# <=50000                 5%


costprice=int(input('enter the price:'))
if costprice>100000:
    print('the tax is 15%')
elif costprice>50000 and costprice<=100000:
    print('the tax is 10%')
else :
    print('the tax is 5% ')

#  A company decided to give bonus to employee according to following criteria:
# Time period of service      Bonus
# More than 10 years          10%
# >=6 and <=10                 8%
# Less than 6 years            5%

timeperiod=int(input('enter the year:'))
if timeperiod>10:
    print('bonous is 10%')
elif timeperiod>=6 and timeperiod<=10:
    print('bonus is 8')
else:
    print('bonus is 5%')


# . Ask the user for a subject score. If it's above 90, congratulate him. If it's between
# 50 and 90, suggest improvement. Otherwise, advise on retaking the course.

subject_score=int(input('enter your subjectscore:'))
if subject_score>=90:
    print('congrulation')
elif subject_score<90 and subject_score>=50:
    print('improvement')
else:
    print('you should study hard')


# Write a program to determine if a candidate is eligible for a job: If the candidate's
# age is >= 18, check if they have a degree. If they have a degree, check their work
# experience: More than 3 years: Display "Highly Eligible." 1-3 years: Display
# "Eligible." Less than 1 year: Display "Under Review."



candiate_age=int(input('enter the age:'))
if candiate_age>=18:
    degree=input('do you have degree?:')
    if degree=='yes':
        experience=int(input('enter the work experience yrs:'))
        if experience>3:
            print('Highly Eligible')
        elif  experience <= 3 and experience >= 1:

            print('eligible')
        else:
            print('Under Review')
    else:
        print('candidate is ineligible')
else:
    print('candidate is ineligible')



#  Accept the age, gender ('M', 'F'), number of days and display the wages
# accordingly.
# Age         Gender           Wage/day
# >=18 and <30   M               700
#                F               750
# >=30 and <=40  M               800
#                F               850


age=int(input('enter the age:'))
if age>=18 and age<30:
    gender=input('enter the gender:')
    if gender=='male':
        print('wage is 700')
    else:
        print('wage is 750')
elif age>=30 and age<=40:
    gender=input('enter the gender:')
    if gender=='male':
        print('wage is  850')
    else:
        print('wage is 800')
else:
    print('no wage')

    
# . Write a Python program to simulate a simple ATM with the following
# specifications:
#  Assume the card is valid (is_valid = True)
#  Initial account balance is 50000
#  Correct PIN is 123
#  After entering correct PIN, display the menu:
# 1. Withdraw
# 2. Check Balance
# 3. Exit
#  If user selects 1 then ask amount and deduct from balance
#  If user selects 2 then show current balance
#  If user selects 3 then print “Thank you for visiting”
#  Show proper messages for wrong PIN and invalid option Use nested if-else
# statements only

pin=int(input('enter the pin nunmber:'))
if pin==123:
    menu=input('enter witndraw or check balance or exit')
   
    if menu=='withdraw':
        amount=input('enter the amount')
        print(f'your {amount} is deduct')
    elif menu=='check balance':
        print("your total amount is 50000")
    else:
        print('Thank you for visiting')
else:
    print('pin is incorrect')


#  Create a Python program that greets the user with the message "Welcome to the
# Magic Forest". Then, ask the user whether they want to go "north" or "south". If
# they choose "south", print "Game Over". If they choose "north", ask if they want to
# "cross the river" or "follow the path". If they choose "cross the river", print "Game
# Over". If they choose "follow the path", ask them to choose between "fairy","ogre",
# or "elf". If they choose "ogre" or "fairy", print "Game Over". If they choose "elf",
# print "You Win".
    

print('welcome to magic forest')
User=input('enter whether you want to go "north" or "south::')

if User=='south':
    print('game over')
else:
    qua=input('do you want to cross the river or follow the path?:')
    if  qua=='cross the river':
        print('game over')
    else:
        Qua=input(' choose between "fairy","ogre",or "elf":')
        if Qua=='ogre' or Qua=="fairy":
            print('game over')
        else:
            print("you won")

     

#  Create a Python program that greets the user with the message "Welcome to the
# Haunted House". Then, ask the user whether they want to go "upstairs" or
# "downstairs". If they choose "downstairs", print "Game Over". If they choose
# "upstairs", ask if they want to "enter the room" or "stay outside". If they choose
# "enter the room", print "Game Over". If they choose "stay outside", ask them to
# choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
# "vampire", print "Game Over". If they choose "werewolf", print "You Win"

print('welcome to Haunted House ')
User=input('do you  want to go "upstairs" or downstairs?:')

if User=='downstairs':
    print('game over')
else:
    qua=input('if they want to "enter the room" or "stay outside::')
    if  qua=='enter the room':
        print('game over')
    else:
        Qua=input('hoose between "ghost", "vampire", or "werewolf":')
        if Qua=='ghost' or Qua=="vampire":
            print('game over')
        else:
            print("you won")

     