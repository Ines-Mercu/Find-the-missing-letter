#https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    dictionary = {}
    for number in seq:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
    for key in dictionary:
        if dictionary[key] % 2 != 0:
            return key
