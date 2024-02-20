def reverse_right_half_pyramid(rows):
    for i in range(rows, 0, -1):
        print("* " * i)


rows = int(input("Enter the number of rows for the pyramid: "))
reverse_right_half_pyramid(rows)
