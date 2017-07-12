# because you apparently need a program to roll a dice for you

from random import randint

play = 0
roll = raw_input('Do you want to roll a dice? (answer Yes or Y or No or N)\n')

while (play == 0):
	if roll == 'Yes' or roll == 'Y':
		min = 1
		max = 6 
		print "The roll of the dice is "
		print(randint(min,max))
		again = raw_input('Would you like to roll again? (answer Yes or Y or No or N)\n')
		if again == 'No':
			print('Thank you for playing!')
			play = 1
		else:
			play = 0

	elif roll == 'No' or roll == 'N': 
		print('Thank you for playing!')
		play = 1

	else:
		print('Your input is not a rolling option.\n Thank you and goodbye!')
		play = 1

		

