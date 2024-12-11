import re
from itertools import islice
import itertools
from collections import Counter


def day1():
    pat = re.compile(r"(\d+)\s{3}(\d+)")

    with open("day1.input") as fp:
        matches = (pat.match(line) for line in fp)
        left, right = itertools.tee(matches, 2)

        left = sorted(m.group(1) for m in left)
        right = sorted(m.group(2) for m in right)

        left = map(int, left)
        right = map(int, right)

        differences = (abs(l - r) for (l, r) in zip(left, right))

        return sum(differences)


def day1_part2():
    pat = re.compile(r"(\d+)\s{3}(\d+)")

    with open("day1.input") as fp:
        matches = (pat.match(line) for line in fp)
        left, right = itertools.tee(matches, 2)

        left = map(int, (m.group(1) for m in left))
        right = map(int, (m.group(2) for m in right))

        lookup = Counter(right)
        similarities = (l * lookup[l] for l in left)

        return sum(similarities)


ans = day1_part2()
print(ans)
