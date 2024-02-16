def horizontal_butterfly_star_pattern(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(n):
            if j < n - i - 1:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    for i in range(1, n):
        for j in range(n):
            if j < n - i:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(n):
            if j < i:
                print(" ", end="")
            else:
                print("*", end="")
        print()


horizontal_butterfly_star_pattern(4)
