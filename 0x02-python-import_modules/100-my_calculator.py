#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        sys.exit(1)
    operator = sys.argv[2]
    if operator == "+":
        print(add(int(sys.argv[1]), int(sys.argv[3])))
    elif operator == "-":
        print(sub(int(sys.argv[1]), int(sys.argv[3])))
    elif operator == "*":
        print(int(mul(sys.argv[1]), int(sys.argv[3])))
    elif operator == "/":
        print(div(int(sys.argv[1]), int(sys.argv[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /i")
        sys.exit(1)
