
rows = 10
cols = 22

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == cols - 1 - (i * (cols - 1) // (rows - 1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
