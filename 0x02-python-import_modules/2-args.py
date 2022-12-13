#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv[1:]
    size = len(user_input)
    # if size == 1:
    #     print("{:d}".format(size), "argument" ":")
    # elif size != 1:
    #     print("{:d}".format(size), "arguments" ".")
    # else:
    #     for i, argv in enumerate(user_input):
    #         print("{:d}: {:s}".format(i + 1, arg))

    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) != 1 else "argument",
                 "." if (size) == 0 else ":"))
    for i, arg in enumerate(user_input):
        print("{:d}: {:s}".format(i + 1, arg))