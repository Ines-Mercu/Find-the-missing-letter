#https://www.codewars.com/kata/5f6d120d40b1c900327b7e22
def leaderboard_sort(leaderboard, changes):
    for name in changes:
        posi = name.split(' ')
        names = posi[0]
        position = leaderboard.index(names)
        leaderboard.remove(names)
        move = int(posi[1])
        leaderboard.insert(position - move, names)
    return leaderboard
