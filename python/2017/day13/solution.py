# Taken from subreddit

from itertools import count as c

def solve(input):
    S = [(d, r, 2*r-2) for d, r in eval(input.strip().replace(*'\n,').join('{}')).items()]
    part1 = sum(d*r for d, r, R in S if not d%R)
    part2 = next(i for i in c() if all((i+d)%R for d, _, R in S))
    return part1, part2

with open('input.txt', 'r') as f:
    print(solve(f.read()))