import ast

#Bibliotheek met Bijbel-teksten en verzen
Bijbel = {}

#bestand word weer gelezen
Lees_bestand = open('C:\\Users\\danny\\OneDrive\\Documenten\\Python Files\\Kleine Projecten\\\Bijbel-vers Spel\\Bijbel.txt')
Invoer = Lees_bestand.read()
Lees_bestand.close()

#maakt van de gelezen string een bibliotheek
Bijbel = ast.literal_eval(Invoer)
print(Bijbel)

#voer nieuwe verzen in en voegt die toe aan de bibliotheek
Vers = 'start' #zodat Vers niet leeg is en loop niet start
while Vers != '':
    Vers = str(input('Geef vers: '))
    Tekst = str(input('Geef tekst: '))
    if Vers != '':
        Bijbel.update({Vers:Tekst})
        pass
    pass

#Bijbel bestand word geschreven
Schrijf_bestand = open('C:\\Users\\danny\\OneDrive\\Documenten\\Python Files\\Kleine Projecten\\\Bijbel-vers Spel\\Bijbel.txt', 'w')
Schrijf_bestand.write(str(Bijbel))
Schrijf_bestand.close()
