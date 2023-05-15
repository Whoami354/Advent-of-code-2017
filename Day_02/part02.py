with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    print(input)


sum = 0

for line in input:
    numbers = [int(number) for number in line.split(" ")]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                continue
            if numbers[i] % numbers[j] == 0:
                sum += (numbers[i] // numbers[j])

print(sum)