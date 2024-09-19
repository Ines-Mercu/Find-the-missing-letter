#https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    numbers = numbers.split(" ")
    high = ""
    low = ""
    for number in numbers:
        if high == "" or int(number) > high:
            high = int(number)
        if low == "" or int(number) < low :
            low = int(number)
    return str(high) + " " + str(low)
