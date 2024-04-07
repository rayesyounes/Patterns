rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    numbers = " ".join(str(i) for _ in range(i))
    print(spaces + numbers)
