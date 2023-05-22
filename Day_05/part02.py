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
idx = 0

input = [int(number) for number in input]

while 0 <= idx < len(input):
    offset = input[idx]
    if offset >= 3:
        input[idx] -= 1
    else:
        input[idx] += 1
    idx += offset
    steps += 1

print(steps)