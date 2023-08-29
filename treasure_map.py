row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Position to change")

vertical = int(position[0])
horizontal = int(position[1])

map[vertical-1][horizontal-1] = 10

print(f"{row1}\n{row2}\n{row3}")
