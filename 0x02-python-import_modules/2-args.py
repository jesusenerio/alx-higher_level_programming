#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    args = len(sys.argv) - 1
    if args == 0:
        print("{} arguments.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
    else:
        print("{} arguments:".format(args))
    while i <= args:
        print("{}: {}".format(i, (sys.argv[i])))
        i += 1
