#this program counts the number of words present in the book Alice In Wonderland

filename = 'alice.txt'

try :
	with open(filename , encoding = 'utf-8') as f :
		contents = f.read()
except FileNotFoundError :
	print(f"Sorry, the file {filename} does not exist.")

else :
	# count the approximate number of words in the file
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")
