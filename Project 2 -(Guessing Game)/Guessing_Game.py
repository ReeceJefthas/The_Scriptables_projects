#import for a random number
import random
#to generate a random number
number = random.randint(1, 50)
print("Im thinking of a number between 1 and 50 ")
guessesTaken = 0
#how much guesses they can have

while guessesTaken < 6:
    guess = input("Enter a guess: ")
    #convert it using int to a number
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        #if guess is less that the number they will get this message
        print("That was too low.")
    elif guess > number:
        # if guess is less that the number they will get this message
        print("That was too high")
    else:
        #equal to the number to exit the loop
        break
#if they guessed correct its equal to the number they get this prompt
if guess == number:
    print("U win")
else:
    #give u the correct number as well
    print("U lose better luck next time,The correct number was", number)


