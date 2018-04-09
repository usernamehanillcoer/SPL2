eingabe = input("Anzahl der Haltestellen eingeben")
eingabe = int(eingabe)
for i in range(1 , eingabe):
  anzahl = input("Wie viele personen steigen ein?: ")
  aussteigen = input("Wie viele personen steigen aus?: ")
  summe = anzahl + anzahl
  summe = anzahl - aussteigen
print("Es sind: ", summe , " personen im bus")
