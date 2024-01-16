def print_reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


num_rows = int(input("Enter the number of rows: "))
print_reverse_pyramid(num_rows)
