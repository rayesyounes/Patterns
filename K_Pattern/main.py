from Reverse_Right_Half_Pyramid.main import reverse_right_half_pyramid
from Right_Half_Pyramid.main import right_half_pyramid

rows = int(input("Enter the number of rows for the pyramid: "))


def main():
    reverse_right_half_pyramid(rows)
    right_half_pyramid(rows)


if __name__ == "__main__":
    main()
