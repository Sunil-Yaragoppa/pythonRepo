'''Programming Poll: Write a while loop that asks people why they like programming. 
Each time someone enters a reason, add their reason to a file that stores all the responses.'''

filename = 'responses.txt'
while True :
	response = input("Why do you love programming ? ")
	if response == 'quit':
		break
	with open(filename , 'a') as file_object :
		file_object.write(response + "\n")
