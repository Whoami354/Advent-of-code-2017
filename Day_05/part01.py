with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    print(input)

steps = 0
index = 0

input = [int(number) for number in input]

while 0 <= index < len(input):
    offset = input[index]
    input[index] += 1
    index += offset
    steps += 1

print(steps)