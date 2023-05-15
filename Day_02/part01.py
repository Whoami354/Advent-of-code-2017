with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    print(input)


sum = 0

for line in input:
    numbers = [int(number) for number in line.split(" ")]
    sum += max(numbers) - min(numbers)

print(sum)