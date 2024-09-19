#https://www.codewars.com/kata/64fbfe2618692c2018ebbddb
def flick_switch(lst):
    switch = 'flick'
    answer = []
    flick = False
    for i in lst:
        if i == switch:
            if flick == False:
                flick = True
            else:
                flick = False
            
        if flick != True:
            answer.append(True)
        else:
            answer.append(False)
    return answer
