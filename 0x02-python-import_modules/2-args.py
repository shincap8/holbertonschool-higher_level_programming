#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arguments = len(sys.argv)
    if arguments == 1:
        print("{:d} arguments.".format(arguments - 1))
    elif arguments > 1:
        if arguments == 2:
            print("{:d} argument:".format(arguments - 1))
            print("1: {}".format(sys.argv[1]))
        else:
            print("{:d} arguments:".format(arguments - 1))
            for i in range(1, arguments):
                print("{:d}: {}".format((i), sys.argv[i]))
