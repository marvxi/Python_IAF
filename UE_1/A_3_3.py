number = int(input("Gib eine beliebige Zahl ein: "))

x = 32
count = 0
while number != x:
    count +=1
    if number > x:
        print("Deine Zahl ist zu Groß!")
    elif number < x:
        print("Deine Zahl ist zu klein!")

    number = int(input("Gib erneut eine Zahl ein: "))

print(f'Spiel gewonnen mit {count} versuchen.')