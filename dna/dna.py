from sys import argv
import csv

if len(argv) !=3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()

db = open(argv[1], "r")#dont touch, this breaks the code
db2= open(argv[1], "r")#dont touch, this breaks the code
db_read = csv.reader(db)#dont touch, this breaks the code
db_read2 = csv.reader(db2)#dont touch, this breaks the code

a= list(db_read)
    
STR=a[0]
STR.pop(0) # removing "name"
num_STR = len(STR)

seq = open(argv[2], "r")
seq_read = seq.read()

count=[]#count[i] = count of STR i in sequence

for z in STR:
    while True:
        for i in range(len(str(seq_read))):
            if str(seq_read).count(z*i) == 0:
                count.append(i-1)
                break
            else:
                continue
            
        break

next(db_read2)
for row in db_read2:
    z = 0
    for i in range(num_STR):
        if str(count[i]) == row[i+1]:
            z += 1
            if z == len(STR):
                print(row[0])
                exit()

print("No match")