#BIRTHDAY DICTIONARY
'''For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.'''

birthday_dict = { 'Sunil' : '09/10/1993' ,
					'Basavaraj' : '12/31/1994' ,
					'Chandan' : '07/02/1994' ,
					'Santosh' : '03/16/1994' ,
					'Benjamin' : '01/17/1706'

}

name = input("Who's birthday do you want to look up?")

print("{}'s birthday is {}".format(name,birthday_dict[name]))
