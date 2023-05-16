with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    print(input)

"""
2
3
2
3
-1
"""

steps = 0
index = 0

input = [int(number) for number in input]

while 0 <= index < len(input):
    offset = input[index]
    if offset >= 3:
        input[index] -= 1
    else:
        input[index] += 1
    index += offset
    steps += 1

print(steps)