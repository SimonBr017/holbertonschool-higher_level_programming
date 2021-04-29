#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    for j in range(1, len(sys.argv)):
        i = i + int(sys.argv[j])
    print(i)
