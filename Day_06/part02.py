with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split()
    print(input)

numbers = [int(num) for num in input]
cycles = 0

for _ in [0]*2:
    seen = set()
    while tuple(numbers) not in seen:
        seen.add(tuple(numbers))
        n = max(numbers)
        i = numbers.index(n)
        numbers[i] = 0
        for j in range(n):
            numbers[(i+j+1) % len(numbers)] += 1

print(len(seen))