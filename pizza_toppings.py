'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
 As they enter each topping, print a message saying you’ll add that topping to their pizza.'''


prompt = "\nEnter your favourite piza topping."
prompt += "\nI will add it to your pizza :  "

active = True

while active :
	pizza = input (prompt)
	
	if pizza != 'quit' :
		print("We will add " + pizza + " to your topping.")
	else :
		active = False
