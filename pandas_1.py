dict = {"country" : {"Brazil" , "Russia" , "India" , "China" , "South Africa"},
		"capital" : {"Brasilia" , "Moscow" , "New Delhi" , "Beiging" , "Pretoria"},
		"area" : {1.8 , 2.1 , 2.4 , 1.18 , 1.45} ,
		"popullation" : {200 , 143 , 1252 , 1357 , 52.98} }
		
import pandas as pd

brics = pd.DataFrame(dict)

print(brics)
