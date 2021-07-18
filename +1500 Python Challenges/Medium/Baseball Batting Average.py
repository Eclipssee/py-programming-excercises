"""
Baseball Batting Average

A baseball player's batting average is calculated by the following formula:

BA = (number of hits) / (number of official at-bats)
Batting averages are always expressed rounded to the nearest thousandth with no leading zero. The top 3 MLB batting averages of all-time are:

Ty Cobb .366
Rogers Hornsby .358
Shoeless Joe Jackson .356
The given list represents a season of games. Each list item indicates a player's [hits, official at bats] per game. Return a string with the player's seasonal batting average rounded to the nearest thousandth.

Examples
batting_avg([[0, 0], [1, 3], [2, 2], [0, 4], [1, 5]]) ➞ ".286"

batting_avg([[2, 5], [2, 3], [0, 3], [1, 5], [2, 4]]) ➞ ".350"

batting_avg([[2, 3], [1, 5], [2, 4], [1, 5], [0, 5]]) ➞ ".273"


Notes
The number of hits will not exceed the number of official at-bats.
The list includes official at-bats only. No other plate-appearances (walks, hit-by-pitches, sacrifices, etc.) are included in the list.
HINT: Think in terms of total hits and total at-bats.
"""



################################################################
"""
Solution 1
"""


def batting_avg(lst):
	a, b = map(sum, zip(*lst))
	return '{:.3f}'.format(a/b)[1:]



################################################################
"""
Solution 2
"""


def batting_avg(l):
    h=b=0
    for x in l:
        h+=x[0]
        b+=x[1]
    return'{}'.format(round(h/b,3)).ljust(5,'0')[1:]




################################################################
"""
Solution 3
"""


def batting_avg(lst):
  res = round(sum([i[0] for i in lst]) / sum([i[1] for i in lst]), 3)
  return str(res)[1:].ljust(4, '0')



#################################################################
"""
Solution 4
"""


def batting_avg(lst):return str(round(sum(list(map(lambda x:x[0],lst)))/sum(list(map(lambda x:x[1],lst))),3))[1:].ljust(4,'0')



