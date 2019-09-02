'''City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this:'''

def city_country(city , country ):
	
	full_name = city.title() + ", " + country.title()
	
	return full_name
	
city_info = city_country('rio de janairo' , 'brazil')

print(city_info)

city_info = city_country('bengaluru' , 'india')

print(city_info)
