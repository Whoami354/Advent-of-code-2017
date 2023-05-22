with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split()
    print(input)

numbers = [int(num) for num in input]
cycles = 0
seen = set()

while tuple(numbers) not in seen:
    seen.add(tuple(numbers))
    maxValue = max(numbers)
    max_index = numbers.index(maxValue)

    numbers[max_index] = 0
    while maxValue > 0:
        max_index = (max_index + 1) % len(numbers)
        numbers[max_index] += 1
        maxValue -= 1

    cycles += 1

print(cycles)