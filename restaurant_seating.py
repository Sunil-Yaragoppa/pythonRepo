'''Restaurant Seating: Write a program that asks the user how many people are in their dinner group.
 If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, 
 report that their table is ready.'''

seat = input ("How many people are in your dinner group ? ")
seat = int(seat)

if seat > 8 :
	print("You will have to wait for the table. ")
	
else :
	print("Yout table is ready.")
