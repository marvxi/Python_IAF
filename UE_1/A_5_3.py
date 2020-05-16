count = 0
while True:
    print(count+1,"Stecke fest!")
    count+=1
    if count >= 10:
        quest = input("Soll nochmal widerholt werden (yes/no)?")
        if quest == "yes":
            count = 0
            continue
        elif quest == "no":
            break
        else:
            print("Eingabe unbekannt, Programm Ende")
            exit()
