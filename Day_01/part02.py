with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read()

#input = ["1122", "1111", "1234", "91212129"]
sum = 0

length = len(input)
step = length // 2


for i in range(length):
    if input[i] == input[(i + step) % length]:
        sum += int(input[i])

print(sum)