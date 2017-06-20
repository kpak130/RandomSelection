
import csv
from random import randint

with open('data.csv', 'rb') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	res = []
	total = 0
	
	for row in data:
		total += int(row[1])
		res.append([row[0],row[1]])
		print "Name: " + row[0] + ", Weight: " + row[1]

	number = randint(0, total-1)

	accumulated = 0
	for data in res:
		accumulated += int(data[1])
		if number <= accumulated:
			print "--------Winner--------"
			print data[0]
			break