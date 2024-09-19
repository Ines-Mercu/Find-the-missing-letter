#https://www.codewars.com/kata/52b757663a95b11b3d00062d
def to_weird_case(words):
    w = words.split(' ')
    answer = ''
    for g in w:
        answer += " "
        l = len(g) 
        for i in range(l):
            if i % 2 == 0:
                answer += g[i].upper() 
            else:
                answer += g[i].lower()
    answer = answer[1: ]
    return answer
