def left_half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print("")


rows = int(input("Enter the number of rows for the pyramid: "))
left_half_pyramid(rows)
