# 1. Create a Python program that prompts the user to enter their age. 
# If the age is less than 18, print "You are a minor." If the age is 
# between 18 and 60, "print "You are an adult. For ages over 60, print 
# "You are a senior citizen." The program should continue until the user 
# inputs "stop."


while True:
    user_input=int(input('enter the age:'))
    if user_input<18:
        print(' you are minor')
    elif user_input>18 and user_input<60:
        print('you are adults')
    elif user_input>60:
        print('You are a senior citizen.')
    else:
        print('stop')


#     2. Write a Python program that simulates waiting for a 
# specific vehicle, such as a "bus". The program should 
# repeatedly prompt the user to input the name of a vehicle. 
# If the input is not "bus", the program should print 
# "waiting" and continue. Once the user inputs "bus", the 
# program should print "finally the wait is over" and terminate the loop.


while (user_input:=input('enter the input:'))!='bus':
 print('watting')
else:
    print('wait is over')


# 3. Write a Python program that continuously prompts the user 
# to input a fruit name. If the input is "apple," the program 
# should print "You got it!" and stop. Otherwise, it should 
# display "Try again" and continue.
         
while True:
    user_input = input("Enter the name of a fruit: ")

    if user_input == "apple":
        print("You got it!")
        break
    else:
        print("Try again")


# 5. Generate a frequency table for the ratings list which is initialized below.
# Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
#     a.	Start by creating an empty dictionary named content_ratings
#     b.	Loop through the ratings list. For each iteration, complete the following:
#         If the rating is already in content_ratings then increment the frequency of that rating by 1.
#         Else, initialize the rating with a value of 1 inside the content_ratings dictionary.

####################################### using for loop###############################################
rating=['4+','5+','4+','9+','3+']
content_rating={}
for i in rating:
    if i in content_rating:
        content_rating[i]=content_rating.get(i,0)+1
    else:
        content_rating[i]=1
print(content_rating)    

###########################################  using while loop################################################
rating=['4+','5+','4+','9+','3+']
content_rating={}
i=0
while i< len(rating):
    if i in content_rating:
        content_rating[rating[i]]=content_rating.get(rating[i],0)+1
    else:
        content_rating[rating[i]]=1
    i+=1
print(content_rating)    


# 6. Write a Python program that generates a random number 
# between 1 and 10 and prompts the user to guess the number. 
# The program should provide hints such as "guess higher" or 
# "guess lower" based on the user's input. Once the user guesses
# the correct number, the program should display the number of 
# attempts it took to guess the correct number


import random
while True:
    rn=random.randint(1,10)
    user_input=int(input('enter a num:'))
    if rn==user_input:
        print('correct num')
        break
    elif user_input>rn:
        print('too high')
    else:
        print('too low')


# 7. Write a Python program that simulates a login system. The program 
# should prompt the user to enter a username and password. If both are 
# correct (e.g., username is "admin" and password is "1234"), 
# print "Login successful" and exit. If either is incorrect, 
# print "Invalid credentials, try again." Allow the user up to 
# 3 attempts before locking them out with the message "Too many failed attempts."

correct_username = "admin"
correct_password = "1234"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        print("Invalid credentials, try again.")
        attempts += 1

if attempts == 3:
    print("Too many failed attempts.")

# . Write a Python program that simulates a basic arithmetic quiz. 
# Generate two random numbers between 1 and 30 and ask the user to 
# provide the result of their multiplication. If the answer is correct, 
# print "Correct!" and generate a new question. If the answer is wrong, 
# print "Incorrect, try again." Allow the user to stop the quiz when the 
# user enters "exit"


import random

while True:
    user_input = input("Press Enter to get a question or type 'exit' to quit: ")

    if user_input.lower() == "exit":
        print("Quiz ended.")
        break

    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)

    answer = int(input(f"What is {num1} × {num2}? "))

    if answer == num1 * num2:
        print("Correct!")
    else:
        print("Incorrect, try again.")

# 9. Write a Python program that prompts the user to enter a number. 
# The program should determine whether the number is prime or not. 
# If the number is prime, print "The number is prime." Otherwise, print
#  "The number is not prime." Continue prompting the user until they enter "

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Program ended.")
        break

    num = int(user_input)

    if num <= 1:
        print("The number is not prime.")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("The number is prime.")
        else:
            print("The number is not prime.")

# 10. Write a Python program that asks the user to guess a pre-defined secret
#  word (e.g., "python"). Provide feedback like "Incorrect, try again" if the 
# guess is wrong. When the user guesses correctly, print "Congratulations, you
#  guessed the word!" Allow the user to exit the program by typing "quit."


secret_word = "python"

while True:
    guess = input("Guess the secret word (or type 'quit' to exit): ")

    if guess.lower() == "quit":
        print("Game exited.")
        break

    if guess == secret_word:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Incorrect, try again.")

# 11. Write a Python program that prompts the user to repeatedly enter a name. 
# If the user enters the phrase "good luck," the program keeps track of how many 
# times the phrase has been entered. When the phrase has been entered three times, 
# the program should display a message stating "You typed good luck three times." 
# For each entry of "good luck" before the third occurrence, display the message 
# "You typed the same word [count] times." Continue this process until the phrase 
# has been entered three times. 


count = 0

while count < 3:
    name = input("Enter a name or phrase: ")

    if name.lower() == "good luck":
        count += 1
        if count < 3:
            print(f"You typed the same word {count} times.")
        else:
            print("You typed good luck three times.")


# 12. Write a Python program that simulates a basic elevator system. The program should keep track of the elevator's current position and allow a user to travel to different floors until they choose to exit.
# Requirements
# a.	Starting State: The elevator should start on floor 1.
# b.	Continuous Loop: Use a while loop to repeatedly ask the user for a destination floor.
# c.	Input Handling: If the user enters 0, the program should print a goodbye message and terminate. If the user enters something that isn't a number, handle the error gracefully so the program doesn't crash.
# d.	Logic: If the target floor is higher than the current floor, print a â€˜Going upâ€™ message. If the target floor is lower than the current floor, print a â€˜Going downâ€™ message. If the user is already on the requested floor, inform them of that. 
# e.	State Update: After "moving," update the current floor to the target floor so the next movement starts from the new location.

current_floor = 1

while True:
    try:
        destination = int(input(f"You are on floor {current_floor}. Enter destination floor (0 to exit): "))

        if destination == 0:
            print("Goodbye!")
            break

        if destination > current_floor:
            print("Going up")
        elif destination < current_floor:
            print("Going down")
        else:
            print("You are already on this floor.")

        current_floor = destination

    except ValueError:
        print("Invalid input. Please enter a number.")
