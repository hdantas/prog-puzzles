# http://www.codewars.com/kata/53837b8c94c170e55f000811

def get_score(dice):
    if sorted(dice) == range(1, 7): return 1000 # straight
    elif [dice.count(die) for die in set(dice)] == 3 * [2]: return 750 # triple pairs
    scores = [1000, 200, 300, 400, 500, 600]
    multiples = [(dice.count(die) - 2) * scores[die - 1] for die in set(dice)] #3+ multiples
    score = sum([item for item in multiples if item > 0]) + \
        (dice.count(1) * 100 if dice.count(1) < 3 else 0) + \
        (dice.count(5) * 50 if dice.count(5) < 3 else 0)
    return score if score > 0 else "Zonk"

print get_score([1,2,3]) # returns 100 = points from one 1
print get_score([3,4,1,1,5]) # returns 250 = points from two 1 and one 5
print get_score([2,3,2,3,3,2]) # returns 500 = three of 2 + three of 3
print get_score([1,1,1,1,1,5]) # returns 3050 = five 1 + one 5
print get_score([2,3,4,3,6,6]) # returns "Zonk" = no combinations here
print get_score([2,2,6,6,2,2]) # returns 400 = four 2, this cannot be scored as three pairs
print get_score([1,3,4,3,4,1]) # returns 750 = three pairs
print get_score([3,3,3,3]) # returns 600 = four of 3
print get_score([1,2,3,4,5]) # returns 150 = it's not straight