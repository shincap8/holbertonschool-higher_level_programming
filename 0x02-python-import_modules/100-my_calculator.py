#!/usr/bin/python3
import sys
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        sys.exit(1)
    operator = sys.argv[2]
    if operator == "+":
        print(add(sys.argv[1], sys.argv[3]))
    elif operator == "-":
        print(sub(sys.argv[1], sys.argv[3]))
    elif operator == "*":
        print(mul(sys.argv[1], sys.argv[3]))
    elif operator == "/":
        print(div(sys.argv[1], sys.argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /i")
        sys.exit(1)
