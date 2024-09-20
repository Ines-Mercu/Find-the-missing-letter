#https://www.codewars.com/kata/55c45be3b2079eccff00010f
def order(sentence):
    if sentence == '':
        return ''
    sentence = sentence.split(' ')
    number ='123456789'
    dict = {}
    for word in sentence:
        for letter in word:
            if letter in number:
                dict[letter] = word
    answer = ''
    print(dict)
    for i in range(1, len(dict) + 1):
        answer += dict[str(i)] 
        answer += ' '
    
    return answer[ :-1]
