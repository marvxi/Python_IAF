krawutschke = {'Vorwissen': 3 , 'Sprachen':['Java','C++'], 'Erwartung': 'Python kennenlernen, Programmierskill verbessern'}


for step,search in enumerate(krawutschke):
    if 'Vorwissen' in krawutschke.keys():
        search = krawutschke['Vorwissen']
        break
print(search)