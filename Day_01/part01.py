with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read()

#input = ["1122", "1111", "1234", "91212129"]
sum = 0

if input[-1] == input[0]:
    sum += int(input[-1])


for i in range(0, len(input) - 1):
    if input[i] == input[i + 1]:
        sum += int(input[i])

print(sum)