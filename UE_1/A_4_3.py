x=[2,4,1,7,6,10,9,5,3,8]


for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j] > x[j+1]:
            x[j+1], x[j] = x[j], x[j+1] # Swap, Argumente links und rechts
print(x)