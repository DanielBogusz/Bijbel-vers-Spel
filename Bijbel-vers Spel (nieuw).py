import ast
import random

bijbel = {} # Bibliotheek met Bijbel-teksten en verzen
antwoorden_map = {'A': 0, 'B': 1, 'C': 2} # mapping van letter naar index

# bestand word gelezen
bestand = open('C:\\Users\\danny\\OneDrive\\Documenten\\Python Files\\Kleine Projecten\\\Bijbel-vers Spel\\Bijbel.txt')
bijbel: dict = ast.literal_eval(bestand.read()) # maakt van de gelezen string een bibliotheek
bestand.close()

aantal = 5 # aantal vragen (variable i.p.v. hardcoded in loop & string)
nog_een_keer = 'j'
while nog_een_keer == 'j':
    vragen = bijbel.copy() # kopieer bijbel zodat het spel opnieuw gespeeld kan worden
    score = 0
    for _ in range(aantal):
        verzen = random.sample(list(vragen.items()), 3) # selecteer 3 willekeurige teksten als Tuple lijst (vers, tekst)
        vers = random.choice(verzen) # kies 1 tekst daarvan om te gaan raden

        # print vraag en antwoorden
        print('Waar staat deze tekst:')
        print(f'{vers[1]}\n')
        for letter, index in antwoorden_map.items(): # itereer over A & 0, B & 1, C & 2 en print zo het juiste item
            print(f'{letter} - {verzen[index][0]}')

        opnieuw = True # loop vlag
        while opnieuw:
            keus: str = input('Antwoord: ').upper()
            if keus not in antwoorden_map.keys():
                print('Geef als antwoord: A, B of C')
                continue
            # map bijv A naar 0, en kijk dan of het willekeurig geselecteerde vers overeenkomt met die op plek 0
            elif verzen[antwoorden_map[keus]] == vers:
                score += 1
                print('Goed geraden!.. Of wist je het gewoon, ;-)\n')
            else:
                print(f'Fout, het juiste antwoord was: {vers[0]}\n')
            opnieuw = False # ga door naar volgende vraag

        vragen.pop(vers[0]) # haal tekst uit mogelijke vragen
    print(f'Je hebt {score} van de {aantal} vragen goed.')
    nog_een_keer = input(f'Nog een keer? (type dan "j"): ')
