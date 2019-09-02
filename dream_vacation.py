'''7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
Write a prompt similar to If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll.'''

dream_vacation = {}

# set a flag to indicate that polling is active 

polling_active = True

while (polling_active) :
	name = input("Enter your name : ")
	dream_place = input ("If you could visit one place in the world, where would you go?  ")
	
	#store the response in a dictionary
	
	dream_vacation[name] = dream_place
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	
	if repeat == 'no' :
		polling_active = False
		
#polling is complete print the results 

for name , place in dream_vacation.items() :
	print(name + " would like to go to " + place)
