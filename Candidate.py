import csv

file = open('data.csv')
data = csv.reader(file)

A = []
compare = []

for row in data:
    A.append(row)

length = len(A[0])-1
General = ['?']*length

temp = []
for row in A:
    if row[length] == "Yes":
        temp.append(row)

hypothesis = []
most = []

for row in A:
    if row[length] == "Yes":
        if hypothesis:
            for index in range(length):
                if hypothesis[index] != row[index]:
                    hypothesis[index] = "?"

            for j in range(length):
                for k in range(len(most)):
                    if most[k][j] != '?' and most[k][j] != hypothesis[j]:
                        del most[k]

        else:
            hypothesis = row[:-1]

    elif row[length] == "No":
        for j in range(length):
            if hypothesis[j] != row[j] and hypothesis[j] != '?':
                General[j] = hypothesis[j]
                print(General)
                most.append(General)
                General = ['?']*length

# print(hypothesis)