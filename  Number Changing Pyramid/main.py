def print_number_pyramid(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()


rows = int(input("Enter the number of rows: "))
print_number_pyramid(rows)
