#Number Guessing Game Python
#Created by SamAyo
import random 
import sys
#play_check function to check if the user is still interested in playing 
#it also check if the user would prefer to change the level of the game instead of closing the game 
#
def play_check(level):
    loop = True 
    while loop is True:
        #checks if the user is still interested in playing the game 
        #level is a variable storing the users choice of level 
        #it checks the value of level and invokes the adequate function
        level_req =str(input("Do  you want to play again? Y?N "))
        req_option= level_req.upper()
        if req_option ==  "Y":
            if level == 1:
                easy()
                break
            elif level == 2:
                medium()
                break
            elif level == 3:
                hard()
                break
        #If the user is no longer interested in that level then this part runs 
        elif req_option == "N":
            while True:
                
                #The user is prompted to decide is he wants to quit the game or not 
                print("Do you want to quit? (Y): ")
                print("Or Select a new level = (N): ")
                x=str(input())
                quit_option= x.upper()
                
                #If the user decides to quit, he gets a farewell greeting and the program ends 
                if quit_option == "Y":
                    print("Thanks for playing!!!")
                    sys.exit()
                
                #If the  user is not interested in quiting he can then change the level of the game
                elif quit_option == "N":
                    print("Choose a new difficulty")
                    #stage function shows the user the list of stages so they can choose 
                    stage()
                    break
                else:
                    print("Enter a valid option Y/N")
        else:
            print("Enter a valid option Y/N")
            break
#A function to generate a random string for a given range 
def random_num(a,b):
    return random.randint(a, b)
    

easy_limit=10
med_limit=20
hard_limit = 50

#A function that controls easy level 
def easy():
    print("""Guess a number between 1 and 10
    You have 6 guess attempts""") 
    number = random_num(1,easy_limit) 
    def check_type():
        global guess
        guess = 0
        loop = True
        while loop is True:
            check=True
            while check is True:
                user_input = input()
                try:
                    guess = int(user_input)
                    break
                except ValueError:
                    print("Invalid input! Enter a number from 1 to 10")
            if guess > easy_limit:
                print("Out of range! Enter a number from 1 to 10")
            else:
                print( "Your guess is " + str(guess))
                break
    chances = 6
    while chances  > 0: 
        
        check_type()   
           
        if guess == number: 
            print(guess)
            # if the user's guess matches the geberated number it prints the user's choice  
            #it also prints a confrimation message and invokes the play check function 
            print("You got it right") 
            play_check(level)

        #Prints a message that tells the user that the guess is wrong                
        else: 
            print("That was wrong")
           
            
            
        # Decrease the value of chance by 1 
        chances -= 1
        print ("You have " + str(chances) + " guesses left")
            
            
   #when the user exhausts his chances 
   # it prints game over and invokes the play check function 
    if chances == 0: 
        print("Game Over!!!") 
        print("The number is", number)
    play_check(level)

#A function that controls medium level
def medium():
    print("""Guess a number (between 1 and 20):
    You have 4 guess attepmts""") 
    number = random_num(1,20) 
    def check_type():
        global guess
        guess = 0
        loop = True
        while loop is True:
            check=True
            while check is True:
                user_input = input()
                try:
                    guess = int(user_input)
                    break
                except ValueError:
                    print("Invalid input! Enter a number from 1 to 10")
            if guess > 20:
                print("Out of range! Enter a number from 1 to 20")
            else:
                print( "Your guess is " + str(guess))
                break
    chances = 4
    while chances  > 0: 
    
        check_type()   
    

        # Compare the user entered number   
        # with the number to be guessed  
        if guess == number: 
            print(guess) 
            print("You got it right") 
            play_check(level)
            break

        else: 
            print("That was wrong")
        
        # Decrease the value of chance by 1 
        chances -= 1
        print ("You have " + str(chances) + " guesses left")
            
    if chances == 0: 
        print("Game Over!!!") 
        print("The number is", number)
        play_check(level)

#A function that controls medium level
def hard():
    print("""Guess a number (between 1 and 50):
    You have 3 guess attepmts""")  
    number = random_num(1,50) 
    def check_type():
        global guess
        guess = 0
        loop = True
        while loop is True:
            check=True
            while check is True:
                user_input = input()
                try:
                    guess = int(user_input)
                    break
                except ValueError:
                    print("Invalid input! Enter a number from 1 to 50")
            if guess > 50:
                print("Out of range! Enter a number from 1 to 50")
            else:
                print( "Your guess is " + str(guess))
                break
    chances = 3
    while chances  > 0: 
        
        
        
        check_type()   
        guess 
        # Compare the user entered number   
        # with the number to be guessed  
        if guess == number: 
            print(guess)
            print("You got it right") 
            play_check(level)
            break

              
        else: 
            print("That was wrong")
           
            
            
        # Decrease the value of chance by 1 
        chances -= 1
        print ("You have " + str(chances) + " chances left")
             
    if chances == 0: 
        print("Game Over!!!") 
        print("The number is", number)
        play_check(level)

#game function is used to invoke various stages of the game depending on the users choice 
    #users choice is stored in a variable named "Level"
def game():
    game=True
    while game is True:
        #Level 1 invokes for easy() to run the game in easy mode 
        if level == 1:
            easy()
        #Level 2 invokes for medium() to run the game in medium mode 
        elif level == 2:
            medium()
            #Level 1 invokes for hard() to run the game in hard mode 
        elif level == 3: 
            hard()
    

#Variables to represent the name of each stage
one = "Easy"
two = "Medium"
three = "Hard"

#stage function shows the user the list of stages so they can choose 
#It also assigns the users choice to the variable 'level' 
# level is later passed as an argument in a different function named "play_check"
def stage():
    print("Number Guessing Game") 
    print("Choose a difficulty level: ")
    print("""
        1. Easy
        2. Medium
        3. Hard """)
    global level
    loop = True
    while loop is True:
        check=True
        while check is True:
            level_choice = input()
            try:
                level = int(level_choice)
                break
            except ValueError:
                print("Invalid input! Enter a number from 1 to 3")
        if level == 1:
            print("Level " + one)
            game()
            break
        elif level == 2:
            print("Level " + two)
            game()
            break
        elif level == 3:
            print("Level " + three)
            game()
            break
        else:
            print("Out of range!!! Choose from option 1 to 3")

stage()
