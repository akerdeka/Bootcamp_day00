import string
import sys


def filterwords(s1, n):
    s2 = s1.split(" ,!?.")
    s3 = []
    for i in s2:
        if len(i) > n:
            s3.append(i)
    print(s3)
    return


if len(sys.argv) != 3:
    print("Error")
if sys.argv[2].isnumeric():
    filterwords(sys.argv[1], int(sys.argv[2]))
else:
    print("Error")
