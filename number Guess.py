#guess the number

#show introduction
#choose random target

target = 10 #start with known value
#initialize a guess counter
guessCounter = 0

#loop forever
while True:
    #ask user for a guess
    userGuess = input('Take a guess: ')
    userGuess = int(userGuess)

    #increment guess counter
    guessCounter = guessCounter

#if users guess is correct, congratulate user, we're done
if userGuess == target:
    print ('you got it!')
    print ('it only took you', guessCounter, 'guess(es).')
    break

#if users guess is too low, tell user
elif userGuess < target:
    print ('your guess was too low.')

#if users guess is too high, tell user
elif userGuess < target:
    print ('your guess was too high.')

#if reached max guess, tell answer correct answer, we're done.
if guessCounter == 5:
    print ('Sorry, you did not get it in 5 guesses')
    print ('The number was:'), target

print ('Thanks for playing')
