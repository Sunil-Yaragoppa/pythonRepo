'''Exercise 16 (and Solution)
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a
new password. Include your run-time code in a main method.'''

import random
import string
from random import sample

# Python program to convert a list 
# of character 
  
def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 
    
lower_case_letters = list(string.ascii_lowercase) 	#store lower case letters in a list
upper_case_letters = list(string.ascii_uppercase)	#store upper case letters in a list
digits_list = list(string.digits)					#store digits 0-9 in a list
punctuation_list = list(string.punctuation)			#store special characters in a list
random.shuffle(lower_case_letters)					#shuffle the characters
random.shuffle(upper_case_letters)
random.shuffle(digits_list)
random.shuffle(punctuation_list)
password = sample(lower_case_letters,3) + sample(upper_case_letters,3) + sample(digits_list,3) + sample(punctuation_list,3)
print(password)
strong_password = convert(password)					#convert list into a string
print(strong_password)
