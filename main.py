count = 0
matrix = [
    ["|1|", "|2|", "|3|"],
    ["|4|", "|5|", "|6|"],
    ["|7|", "|8|", "|9|"]
]

winner = False
while count <= 9:
    BREAK = True
    diagonal1 = []
    diagonal2 = []

    rows = []
    columns = []

    for row in range(3):
        for column in range(3):
            print(f"{matrix[row][column]}", end=" ")
        print("\n")

    while (BREAK):
        if count == 0 or count % 2 == 0:
            pos = int(input("Enter X"))
            for row in range(3):
                for column in range(3):
                    try:
                        if ((int((matrix[row][column]).split('|')[1]) == pos)):
                            matrix[row][column] = "|X|"
                            BREAK = False
                    except ValueError:
                        print("again")
                        pass



        else:
            pos = int(input("Enter 0"))
            for row in range(3):
                for column in range(3):
                    try:
                        if ((int((matrix[row][column]).split('|')[1]) == pos)):
                            matrix[row][column] = "|O|"

                            BREAK = False
                    except ValueError:

                        pass

    # row check
    for i in range(3):
        if (matrix[i] == ["|X|", "|X|", "|X|"]):
            print("X IS WINNER")
            winner = True
            break
        if (matrix[i] == ["|O|", "|O|", "|O|"]):
            print("0 IS WINNER")
            winner = True
            break

    if (winner):
        break

    # diagonal1 check
    for row in range(3):
        diagonal1.append(matrix[row][row])

    if (diagonal1 == ["|X|", "|X|", "|X|"]):
        print("X IS WINNER")
        winner = True
        break
    if (diagonal1 == ["|O|", "|O|", "|O|"]):
        print("0 IS WINNER")
        winner = True
        break

    if (winner):
        break

        # diagonal2 check
    for row in range(3):
        diagonal2.append(matrix[row][3 - row - 1])

    if (diagonal2 == ["|X|", "|X|", "|X|"]):
        print("X IS WINNER")
        winner = True
        break
    if (diagonal2 == ["|O|", "|O|", "|O|"]):
        print("0 IS WINNER")
        winner = True
        break

    if (winner):
        break

    for column in range(3):
        columncheck = []
        for row in range(3):
            columncheck.append(matrix[row][column])
        if (columncheck == ["|X|", "|X|", "|X|"]):
            print("X IS WINNER")
            winner = True
            break
        if (columncheck == ["|O|", "|O|", "|O|"]):
            print("0 IS WINNER")
            winner = True
            break

    if (winner):
        break

    count = count + 1