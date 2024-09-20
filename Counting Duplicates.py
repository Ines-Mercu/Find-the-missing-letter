#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
def duplicate_count(text):
    text = text.lower()
    dic = {}
    count = 0
    for letter in text: 
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    for key in dic:
        if dic[key] > 1:
            count += 1 
    return count
