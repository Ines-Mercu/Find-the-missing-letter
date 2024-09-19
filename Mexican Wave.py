#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
def wave(people):
    array = []
    for x in range(len(people)):
        if people[x] == " ":
            continue
        tmp = list(people)
        tmp[x] = tmp[x].upper()
        array.append(''.join(tmp))

        
    return array
