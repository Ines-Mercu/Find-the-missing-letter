#https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
    n = str(n)
    while len(n) > 1:
        answer = 0
        for number in n:
            answer += int(number)
        n = str(answer)
    return int(n)
