import ast
import random


#Bibliotheek met Bijbel-teksten en verzen
Bijbel = {}

#bestand word weer gelezen
Lees_bestand = open('C:\\Users\\danny\\OneDrive\\Documenten\\Python Files\\Kleine Projecten\\\Bijbel-vers Spel\\Bijbel.txt')
Invoer = Lees_bestand.read()
Lees_bestand.close()

#maakt van de gelezen string een bibliotheek
Bijbel = ast.literal_eval(Invoer)

nog_een_keer = ('j')

while nog_een_keer == 'j':
 vraag_lijst = list(range(0,len(Bijbel))) #maakt een lijst met aantal mogelijke vragen
 antwoord_lijst = vraag_lijst.copy()

 score = 0
 x = 0
 while x < 5: #het aantal vragen dat gesteld gaat worden
     x = x + 1

     vraag = random.choice(vraag_lijst) #willekeurig vraag uit vragenlijst
     print('Waar staat deze tekst:')
     vraag_tekst = list(list(Bijbel.items())[vraag]) #haal de bijvelvers en tekst uit de bibliotheek Bijbel
     print(f'{vraag_tekst[1]}\n') #print de tekst op het scherm

     keuze_lijst = antwoord_lijst.copy() #de keuze voor mogelijke antwoorden is de complete lijst
     keuze_lijst.remove(vraag) #het vraag wordt uit de mogelijke keuzes gehaald

     keuze_2 = random.choice(keuze_lijst) #willekeurige antwoord mogelijkheid 2
     keuze_tekst = list(list(Bijbel.items())[keuze_2]) #haalt de willekeurige antwoord uit de Bijbel bibliotheek
     vraag_tekst.extend({keuze_tekst[0]}) #zet het willekeurige 'foute' antwoord in de vraar_tekst lijst
     keuze_lijst.remove(keuze_2) #gekozen willekeurig antwoord word uit de mogelijke keuzes gehaald

     keuze_3 = random.choice(keuze_lijst) #willekeurige antwoord mogelijkheid 3
     keuze_tekst = list(list(Bijbel.items())[keuze_3]) #haalt de willekeurige antwoord uit de Bijbel bibliotheek
     vraag_tekst.extend({keuze_tekst[0]}) #zet het willekeurige 'foute' antwoord in de vraar_tekst lijst

     antwoord = [0,2,3] #maakt een lijst van de 'mogelijke' antwoorden
     random.shuffle(antwoord) #zet de 'mogelijke' antwoorden door elkaar

     print(f'A - {vraag_tekst[antwoord[0]]}') #print de mogelijke antwoorden uit
     print(f'B - {vraag_tekst[antwoord[1]]}')
     print(f'C - {vraag_tekst[antwoord[2]]}')

     opnieuw = 1 #vlag voor de loop

     while opnieuw == 1:

      keus = input('Antwoord: ') #invoeren van het antwoord
      keus = keus.upper() #zorgt ervoor dat het hoofdletters worden
      if keus == 'A': #wanneer opgaven 'A' is
         keuze = vraag_tekst[antwoord[0]] #dan is het de eerst antwoord mogelijkheid

         if str(keuze) == str(vraag_tekst[0]): #wanneer het antwoord hetzelfde is als die bij de vraag hoort
            score = score + 1 #dan wordt de score met 1 put verhoogd
            print('Goed geraden!.. Of wist je het gewoon, ;-)\n')
         else:
             print(f'Fout, het juiste antwoord was: {vraag_tekst[0]}\n')
         opnieuw = 0 #doe dan de loop niet opnieuw, maar ga door naar de volgende vraag

      elif keus == 'B':
         keuze = vraag_tekst[antwoord[1]]
         if str(keuze) == str(vraag_tekst[0]):
             score = score + 1
             print('Goed geraden!.. Of wist je het gewoon, ;-)\n')
         else:
             print(f'Fout, het juiste antwoord was: {vraag_tekst[0]}\n')
         opnieuw = 0


      elif keus == 'C':
         keuze = vraag_tekst[antwoord[2]]
         if str(keuze) == str(vraag_tekst[0]):
             score = score + 1
             print('Goed geraden!.. Of wist je het gewoon, ;-)\n')
         else:
             print(f'Fout, het juiste antwoord was: {vraag_tekst[0]}\n')
         opnieuw = 0


      else:
          print('Geef als antwoord: A, B of C')
          opnieuw = 1



     vraag_lijst.remove(vraag) #de vraag woord uit de mogelijke vragenlijst gehaald
 print(f'Je hebt {score} van de 5 vragen goed.')
 nog_een_keer = input(f'Nog een keer? (type dan "j"): ')
