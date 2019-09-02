'''Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in 
Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of 
strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of privileges. 
Create an instance of Admin, and call your method.'''

'''Users: Make a class called User. 
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user'''

'''Privileges: Write a separate Privileges class. 
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.'''

class User():
	def __init__(self , first_name , last_name , city):
		self.first_name = first_name
		self.last_name = last_name
		self.city = city
		
	def describe_user(self):
		print(self.first_name.title())
		print(self.last_name.title())
		print(self.city.title())
		
class Privileges():
	def __init__(self):
		self.privileges = ['can add post' , 'can delete post' , 'can ban user' , 'can install an application']
		
	def show_privileges(self):
		print(self.privileges)
		
		
#user1 = User('sunny' , 'yaragoppa' , 'bangalore')
#user1.describe_user()

class Admin (User):
	def __init__(self , first_name , last_name , city):
		super().__init__(first_name , last_name , city)
		self.privileges = Privileges()
		
	'''def show_privileges(self):
		print(self.privileges)'''
		
user_admin = Admin('sunny' , 'yaragoppa' , 'bangalore')

#user_admin.describe_user()

user_admin.privileges.show_privileges()

