values = []
target = 4
values = [2,1,5,3]
for i in range(len(values)-1):
    for j in range(i+1,(len(values))):
        if (values[i]+values[j] == target):
            print(i,j)