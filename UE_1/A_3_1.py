
MyText = open('MyText.txt','r')
MyText = MyText.read()
)

Search = input("Gebe das Suchwort ein: ")
Locat = MyText.find(Search)
Counts = MyText.count(Search)

if Locat>=0:
    print(f'Das gesuchte Wort: \"{Search}\" wurde {Counts}-mal gefunden\nerste Fundstelle: {Locat}')
else:
    print(f'Das gesuchte Wort: \"{Search}\" wurde nicht gefunden')