#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    i = 0
    if c % 2 == 1:
        i = -32
    print("{}".format(chr(c + i)), end="")
