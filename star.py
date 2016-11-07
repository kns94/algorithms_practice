#from __future__ import print_function
import sys


def pattern(n):
    if n == 1:
        return '*'


    for i in range(1, n):
        j = i
        while j <= n:
            j += 1


if __name__ == "__main__":
    n = int(sys.argv[1])
    print pattern(n)