'''Restaurant: Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''

'''Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171).
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.'''

class Restaurant():
	def __init__(self , restaurant_name , cuisine_type):
		self.restaurant_name  = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(self.restaurant_name.title())
		print(self.cuisine_type.title())
		
	def open_restaurant(self):
		print("The restaurant is open!")
		
		
#restaurant = Restaurant('the grand budapest' , 'luxury')

#restaurant.describe_restaurant()
#restaurant.open_restaurant()

class IceCreamStand(Restaurant):
	def __init__(self , restaurant_name , cuisine_type):
		super().__init__( restaurant_name , cuisine_type)
		self.flavours = ['strawberry' , 'chocolate' , 'pista' , 'butter scotch']
	
	def show_flavours(self):
		print(self.flavours)

restaurant  = IceCreamStand('the grand budapest' , 'luxury')

restaurant.show_flavours()
