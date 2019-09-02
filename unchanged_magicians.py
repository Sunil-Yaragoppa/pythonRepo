'''Unchanged Magicians: Start with your work from Exercise 8-10. 
Call the function make_great() with a copy of the list of magicians’ names. 
Because the original list will be unchanged, return the new list and store it in a separate list. 
Call show_magicians() with each list to show that you have one list of the original names and one list with 
the Great added to each magician’s name.'''

def show_magicians (the_great_magicians) :
	for name in the_great_magicians:
		print(name.title())
		
def make_great(magician_names, the_great_magicians):
	while magician_names :
		current_magician = "the great " + magician_names.pop()  # append and add the phrase the great
		
		the_great_magicians.append(current_magician)
	
the_great_magicians = []
magician_names = ['robert' , 'jane' , 'avi' , 'hodor' , 'red woman']
make_great(magician_names[:] , the_great_magicians)
show_magicians(the_great_magicians)
show_magicians(magician_names)
