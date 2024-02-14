rows = int(input("Enter the number of rows: "))


def print_rhombus_pattern(rows):
    for i in range(rows):
        print(" " * (i * 2), end="")
        print("* " * 4)


print_rhombus_pattern(rows)
