import re, math
import itertools


def is_report_valid(report: list[int]) -> bool:
    a, b = map(list, itertools.tee(report))
    b.pop(0)

    differences = [first - second for (first, second) in zip(a, b)]

    a = set([1, 2, 3])
    b = set([-1, -2, -3])

    return set(differences).issubset(a) or set(differences).issubset(b)


def day3():
    pat = re.compile(r"mul\((\d+),(\d+)\)")

    with open("day3.input") as fp:
        ans = 0
        for line in fp:
            for pair in pat.findall(line):
                ans += math.prod(map(int, pair))

        return ans


def day3_part2():
    pat = re.compile(r"mul\((\d+),(\d+)\)")

    with open("day3.input") as fp:
        ans = 0
        lines = fp.readlines()
        lines = ''.join(lines)

        blocks = lines.split("don't()")
        for pair in pat.findall(blocks[0]):
            ans += math.prod(map(int, pair))

        for block in blocks[1:]:
            more_blocks = block.split("do()")

            # skip the first one because its the part that is
            # contained between don't() and do()
            # this also has the benefit of making this exit early if no 'do()' is found (since that will mean len(more_blocks) == 1)
            blocks2 = ''.join(more_blocks[1:])
            for pair in pat.findall(blocks2):
                ans += math.prod(map(int, pair))

        return ans


print(day3_part2())
