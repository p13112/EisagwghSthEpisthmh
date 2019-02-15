a = [int(x) for x in input().split()] #Η εισαγωγή δε χρειάζεται μορφολογία λίστας.


max = sum(a)
l = a[:]
for start in range(len(a)):
    for end in range(start, len(a)):
        s = sum(a[start:end+1])
        if s > max:
            max = s
            l = a[start:end+1]
print(max, l) ;


