def print_increasing_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


n = int(input("Enter the number of rows:"))
print_increasing_pyramid(n)
