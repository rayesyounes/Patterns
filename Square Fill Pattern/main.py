def print_square_fill_pattern(size, fill_char):
    for i in range(size):
        for j in range(size):
            print(" " + fill_char, end=" ")
        print()


size = int(input("Enter the size of the square: "))
fill_char = input("Enter the character to fill the square: ")

print("Square Fill Pattern:")
print_square_fill_pattern(size, fill_char)
