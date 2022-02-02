import csv

file = open('data.csv')
data = csv.reader(file)

temp = []

for row in data:
    if row[-1] == 'Yes':
        temp.append(row[:-1])

length = len(temp[0])

hypothesis = []

for instance in temp:
    if hypothesis:
        for i in range(length):
            if hypothesis[i] != instance[i]:
                hypothesis[i] = "?"
    else:
        hypothesis = instance

print(hypothesis)