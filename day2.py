import re
import itertools


def is_report_valid(report: list[int]) -> bool:
    a, b = map(list, itertools.tee(report))
    b.pop(0)

    differences = [first - second for (first, second) in zip(a, b)]

    a = set([1, 2, 3])
    b = set([-1, -2, -3])

    return set(differences).issubset(a) or set(differences).issubset(b)


def day2():
    pat = re.compile(r"(\d+)")

    with open("day2.input") as fp:
        reports = [list(map(int, pat.findall(line))) for line in fp]

        answers = list(map(is_report_valid, reports))

        return sum(map(int, answers))


def day2_part2():
    pat = re.compile(r"(\d+)")

    with open("day2.input") as fp:
        reports = [list(map(int, pat.findall(line))) for line in fp]

        answers = list(map(is_report_valid, reports))
        good_so_far = sum(map(int, answers))

        extra_good_ones = 0
        for i, ans in enumerate(answers):
            if ans:
                continue

            report = reports[i]
            duplicates = itertools.tee(report, len(report))

            for j, duplicate_report in enumerate(duplicates):
                new_report = list(duplicate_report)
                new_report.pop(j)
                new_ans = is_report_valid(new_report)
                if new_ans:
                    extra_good_ones += 1
                    break

        return good_so_far + extra_good_ones


print(day2_part2())
