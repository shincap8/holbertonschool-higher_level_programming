#!/usr/bin/python3
def weight_average(my_list=[]):
    divisor = 0
    mul = 1
    dividend = 0
    flag = 0
    if my_list:
        for i in my_list:
            for j in i:
                mul = mul * j
                if flag == 1:
                    flag = 0
                    divisor = divisor + j
                else:
                    flag = 1
            dividend = dividend + mul
            mul = 1
        return (dividend / divisor)
    else:
        return 0
