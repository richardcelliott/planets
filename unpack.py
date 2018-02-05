import csv
with open('contributors.txt', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		print row

