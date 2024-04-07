def reverse_left_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i), "*" * i)


rows = int(input("Enter the number of rows for the pyramid: "))
reverse_left_pyramid(rows)
