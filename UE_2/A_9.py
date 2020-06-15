import random as r

while True:
    print(r.randint(1,7))
    choose = input("Soll erneut gewüfelt werden?(Yes/No)")
    if choose == 'No':
        break