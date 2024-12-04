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
    dont_pattern = re.compile(r"don't\(\)")
    do_pattern = re.compile(r"do\(\)")
    disabling_pattern = re.compile(r"don't\(\).*?do\(\)")

    with open("day3.input") as fp:
        ans = 0
        for line in fp:
            new_line = re.sub(disabling_pattern, "", line)

            for pair in pat.findall(new_line):
                ans += math.prod(map(int, pair))

        return ans


print(day3_part2())
