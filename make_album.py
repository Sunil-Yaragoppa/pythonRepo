'''Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album information correctly.
Add an optional parameter to make_album() that allows you to store the number of tracks on an album. 
If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of tracks on an album.'''

def make_album(artist_name, album_title, number_of_tracks = ''):
	
	album = { 'artist_name' : artist_name.title() ,
	'album_title' : album_title.title() , 
	}
	
	if number_of_tracks :
		album['number_of_tracks'] = number_of_tracks
		
	return album
	
album1 = make_album('j balvin' , 'vibras')
album2 = make_album('camila cabello' , 'camila')
album3 = make_album('travis scott' , 'astraworld' , 26)
album4 = make_album('janelle monae' , 'dirty computer' , 8)

print (album1)
print (album2)
print (album3)
print (album4)
