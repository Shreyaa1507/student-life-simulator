def grid(filepath):
    """Read a campus map file into a grid."""
    with open(filepath, "r") as file:
        campus_map = []

        for line in file:
            line = line.strip()
            row = []

            for char in line:
                if char in [".", "#", "R"]:
                    row.append(char)
                else:
                    row.append("#")

            campus_map.append(row)

    return campus_map


def search(campus_map, current_position):
    """Search the campus map for a room from the current position."""
    row, column = current_position

    if row < 0 or row >= len(campus_map) or column < 0 or column >= len(campus_map[row]):
        return False

    current_cell = campus_map[row][column]

    if current_cell == "#" or current_cell == "C":
        return False

    if current_cell == "R":
        print(f"Found room at {row}, {column}")
        return True

    campus_map[row][column] = "C"

    directions = [
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1),
    ]

    for row_change, col_change in directions:
        next_row = row + row_change
        next_col = column + col_change

        if 0 <= next_row < len(campus_map) and 0 <= next_col < len(campus_map[next_row]):
            next_cell = campus_map[next_row][next_col]

            if next_cell == ".":
                print(f"{next_row}, {next_col}")

                if search(campus_map, (next_row, next_col)):
                    return True
            elif next_cell == "R":
                if search(campus_map, (next_row, next_col)):
                    return True

    return False
