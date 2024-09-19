#https://www.codewars.com/kata/5507309481b8bd3b7e001638
import math
def number_property(n):
    answer = []
    if n < 2:
        answer.append(False)
    else:
        for i in range(2,int(math.isqrt(n)+1)):
            if n % i == 0:
                answer.append(False)
                break
    if len(answer) == 0:
        answer.append(True)
    if n % 2 == 0:
        answer.append(True)
    else:
        answer.append(False)
        
    if n % 10 == 0:
        answer.append(True)
    else:
        answer.append(False)
        
    return answer 
