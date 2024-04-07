def reverse_right_half_pyramid(rows):
    for i in range(rows, 0, -1):
        print("* " * i)


def get_input_and_print_pyramid():
    rows = int(input("Enter the number of rows: "))
    reverse_right_half_pyramid(rows)

def main():
    get_input_and_print_pyramid()


if __name__ == "__main__":
    main()
