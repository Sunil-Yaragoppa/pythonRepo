with open('pi_million_digits.txt') as file_object:
	lines = file_object.readlines()
pi_string = ''	
for line in lines:
	pi_string += line.strip()
	
#print(pi_string)
#print(len(pi_string))

birthday = input("Enter your birthday in the form mmddyy : ")
if birthday in pi_string :
	print("Your birthday appears in the first million digits of Pi!")
else:
	print("Your birthday doesn't appear in the first million figits of Pi!")
