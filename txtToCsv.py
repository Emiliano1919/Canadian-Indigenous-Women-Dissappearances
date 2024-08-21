import csv

input_file = 'manual.txt'  
output_file = 'output.csv'  

with open(input_file, 'r') as infile:
    lines = infile.readlines()

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    for line in lines:
        
        columns = line.split()#Default to split on whitespace

        writer.writerow(columns)