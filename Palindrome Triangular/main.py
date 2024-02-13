rows = int(input("Enter the number of rows: "))


def palindromic_triangular(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")

        for j in range(i, 0, -1):
            print(j, end="")

        for j in range(2, i + 1):
            print(j, end="")

        print()


palindromic_triangular(rows)
