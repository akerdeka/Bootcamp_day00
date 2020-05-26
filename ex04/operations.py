import sys
import string


def operations(n1, n2):
    print(n1 + n2)
    print(n1 - n2)
    print(n1 * n2)
    if n2 == 0:
        print("Error (div by zero)")
    else:
        print(n1 / n2)
    if n2 == 0:
        print("Error (modulo by zero)")
    else:
        print(n1 % n2)
    return


if len(sys.argv) != 3:
    print("Only 2 numbers")
elif sys.argv[1].isnumeric() & sys.argv[2].isnumeric():
    operations(int(sys.argv[1]), int(sys.argv[2]))
else:
    print("Only numbers")
