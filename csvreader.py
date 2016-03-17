import csv
week46 = list()
category = list()
data = list()
with open('WeeklyTotals.csv') as csvfile:

	reader = csv.reader(csvfile)
	for row in reader:
		data.append(row)


for x in range(0,len(data)):
    category.append(data[x][0])

num_weeks = (len(data[1]) - 1)/2

print('test')
print( num_weeks )
print(category)
