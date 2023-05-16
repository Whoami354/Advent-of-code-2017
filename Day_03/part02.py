def find_first_value_larger_than_input(input_value):
    grid = {(0, 0): 1}  # Initialisiere das Gitter mit Quadrat 1 als Startwert
    x = 0
    y = 0

    direction = 0  # 0: rechts, 1: oben, 2: links, 3: unten
    length = 1
    count = 0

    while True:
        value = get_adjacent_sum(grid, x, y)
        grid[(x, y)] = value

        if value > input_value:
            return value

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

def get_adjacent_sum(grid, x, y):
    adjacent_sum = 0
    adjacent_positions = [(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2)]
    for position in adjacent_positions:
        if position in grid:
            adjacent_sum += grid[position]
    return adjacent_sum

# Beispielaufruf mit der gegebenen Eingabe
input_value = 347991
result = find_first_value_larger_than_input(input_value)
print(f"Erster Wert größer als die Eingabe: {result}")
