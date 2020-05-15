x = []
for i in range(11):
    x.append(i)

# Stümperlösung
for i in range(1,len(x)):
    print('| x%d ' %(x[i]),end='')
print('|',end='')
print('\n')
print('-----------------------------------------------------',end='')
print('\n')

for i in range(1,len(x)):
    print('|  %d ' %(x[i]),end='')
print('|', end='')
print('\n')

#---------Lösung
print('| x1\t| x2\t| x3\t| x4\t| x5\t| x6\t| x7\t| x8\t| x9\t| x10\t|')
print('---------------------------------------------------------------------------------')
print(f'| {x[1]}\t\t| {x[2]}\t\t| {x[3]}\t\t| {x[4]}\t\t| {x[5]}\t\t| {x[6]}\t\t| {x[7]}\t\t| {x[8]}\t\t| {x[9]}\t\t| {x[10]}\t|')

