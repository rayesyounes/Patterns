def square_hollow_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Change the value of n to adjust the size of the square
n = int(input("Enter the size of the square: "))
square_hollow_pattern(n)
