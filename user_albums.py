
'''User Albums: Start with your program from Exercise 8-7.
 Write a while loop that allows users to enter an album’s artist and title. 
 Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
  Be sure to include a quit value in the while loop.'''
  

def make_album(artist_name, album_title, number_of_tracks = 25):
	
	album = { 'artist_name' : artist_name.title() ,
	'album_title' : album_title.title() , 
	}
		
	return album
	
while True: 
	print("\nEnter an album's artist and title ")
	print("\n(Enter 'q' at any time to quit )")
	
	artist_name = input("\nEnter album's artist : ")
	if artist_name == 'q' :
		break
		
	album_title = input ("\nEnter title of the album : ")
	if album_title == 'q' :
		break
	album1 = make_album(artist_name , album_title)
	
	print("\n")
	print (album1)
	
