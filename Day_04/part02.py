with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    print(input)

counter = 0

for line in input:
    words = line.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    if len(words) == len(set(sorted_words)):
        counter += 1

print(counter)