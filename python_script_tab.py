import csv        
with open('data.tsv','r') as csvin, open('new_data.tsv', 'w') as tsvout:
    csvin = csv.reader(csvin)      
    tsvout = csv.writer(tsvout, delimiter='\t') 
    
    for row in csvin:
		tsvout.writerow(row)   
