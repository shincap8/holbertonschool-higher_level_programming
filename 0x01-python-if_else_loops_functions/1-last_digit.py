#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
text = "Last digit of"
if number < 0:
    last_d = ((number * -1) % 10) * -1
else:
    last_d = number % 10
if last_d > 5:
    print(text, number, ' is ', last_d, 'and is greater than 5')
elif last_d == 0:
    print(text, number, ' is ', last_d, 'and is 0')
else:
    print(text, number, ' is ', last_d, 'and is less than 6 and not 0')
