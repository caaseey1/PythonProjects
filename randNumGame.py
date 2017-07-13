#guess the number! between 1 - 20 (can adjust accordingly)

from random import randint

max = 20 #adjust as desired
min = 1
play = 0
answer = randint(min,max)
print answer

while (play == 0): 
	guess = input('Guess a number between 1 and 20\n')
	# testing only print "You guessed:",guess
	if guess > answer: 
		print "Your guess of",guess,"is greater than the answer, guess again!"
		play = 0
	elif guess < answer:
		print "Your guess of",guess,"is less than the answer, guess again!"
		play = 0
	else:
		print "Your guess of",guess,"is correct! You win!"
		play = 1
