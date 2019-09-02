'''10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file 
and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. 
Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
Move one of the files to a different location on your system, and make sure the code in the except block executes properly.'''

def word_count(filename):
	'''Count the approximate number of words in a file'''
	try:
		with open(filename , encoding = 'utf-8') as f :
			contents = f.read()
	except FileNotFoundError :
		print(f"Sorry , file {filename} does not exist.")
	else:
		words = contents.split()
		num_words = len(words)
		print(f"File {filename} has  about {num_words} words. ")
		
filenames = ['dogs.txt' , 'cats.txt' , 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	word_count(filename)

