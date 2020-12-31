import random

def computerGuess(lowval, highval, randnum, count = 0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess==randnum:
            return count
        # if guess is greater than the number
        # it must be found in lower set of numbers
        # between the loweval and guess
        elif guess > randnum:
            count += 1
            return computerGuess(lowval, guess - 1, randnum, count)
        else:

            #number must be in higher set of number
            #between the guess and upper value
            count += 1
            return computerGuess(guess + 1, highval, randnum, count)
    else:
        #lowval >= highval will also not true
        return -1
#generate the random number b/w 1 and 100
randnum = random.randint(1,101)

count = 0
guess = -99

while guess != randnum:
    #get the user's guess
    guess = int(input("enter the number b/w 1 and 100: "))
    if guess <  randnum:
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print("you guessed right")
        break
    count += 1
print("you took " + str(count) + " " +"chances to guess it right")
print("computer took " + str(computerGuess(0,100,randnum)) + " " +"steps!")