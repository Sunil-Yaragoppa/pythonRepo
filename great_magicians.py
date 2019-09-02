'''Great Magicians: Start with a copy of your program from Exercise 8-9. 
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. 
Call show_magicians() to see that the list has actually been modified.'''

def show_magicians (the_great_magicians) :
	for name in the_great_magicians:
		print(name.title())
		
def make_great(magician_names , the_great_magicians):
	while magician_names :
		current_magician = "the great " + magician_names.pop()  # append and add the phrase the great
		
		the_great_magicians.append(current_magician)
	
the_great_magicians = []
magician_names = ['robert' , 'jane' , 'avi' , 'hodor' , 'the red woman']
make_great(magician_names , the_great_magicians)
show_magicians(the_great_magicians)

#print(the_great_magicians)
#print(magician_names)
