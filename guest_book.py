'''Guest Book: Write a while loop that prompts users for their name. 
When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. 
Make sure each entry appears on a new line in the file.'''


filename = 'guest_book.txt'
while True :
	guest_name = input("Enter your name : ")
	if guest_name == 'quit' :
		break
	with open(filename , 'a') as file_object:
		file_object.write(guest_name + "\n")
	print("Welcome , " , guest_name)
	
		
