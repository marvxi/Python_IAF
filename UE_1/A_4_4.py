MyText = open('MyText.txt','r')
MyText = MyText.read()

Search = input("Gebe das Suchwort ein: ")
Counts = MyText.count(Search)
Locat = MyText.find(Search)

if Locat >= 0:
    print(f'Das gesuchte Wort: \"{Search}\" wurde {Counts}-mal gefunden\nerste Fundstelle: {Locat}')
    if Counts > 1:
        for i in range(Counts-1):
            tmp = Locat+len(Search)
            Locat=MyText[tmp:].find(Search)
            Locat=Locat+tmp
            print(f"weitere Fundstelle: {Locat}")
else:
    print(f'Das gesuchte Wort: \"{Search}\" wurde nicht gefunden')