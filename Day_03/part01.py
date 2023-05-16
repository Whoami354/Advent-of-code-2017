def calculate_steps(square):
    # Berechne die Koordinaten des Quadrats
    x, y = get_coordinates(square)

    # Berechne die Manhattan-Distanz zur Zugriffstür (Quadrat 1)
    steps = abs(x) + abs(y)

    return steps

def get_coordinates(square):
    if square == 1:
        return 0, 0

    # Initialisiere die Variablen
    x = 0
    y = 0
    direction = 0  # 0: rechts, 1: oben, 2: links, 3: unten
    length = 1
    count = 0

    for num in range(2, square + 1):
        if direction == 0:
            x += 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x -= 1
        elif direction == 3:
            y -= 1

        count += 1

        if count == length:
            count = 0
            direction = (direction + 1) % 4
            if direction == 0 or direction == 2:
                length += 1

    return x, y

# Beispielaufruf mit der gegebenen Eingabe
input_square = 347991
steps = calculate_steps(input_square)
print(f"Anzahl der Schritte: {steps}")
