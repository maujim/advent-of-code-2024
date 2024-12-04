import re, math
import itertools


def day4():
    target = "XMAS"
    pat = re.compile(r"(?=XMAS|SAMX)")

    with open("day4.test") as fp:
        rows = [l.strip() for l in fp]
        cols = ["".join((row[x] for row in rows)) for x in range(len(rows))]

        # ensure all rows are same len, and all cols are same length
        assert 1 == len(set(map(len, rows)))
        assert 1 == len(set(map(len, cols)))

        print(f"word search has {len(cols)} columns and {len(rows)} rows")

        def make_diagonal(ri, ci, mode="backslash"):
            assert mode in ["backslash", "forwardslash"]

            buf = ""

            row_bounds = list(range(len(rows)))
            col_bounds = list(range(len(cols)))

            while ri in row_bounds and ci in col_bounds:
                buf += rows[ri][ci]
                ri += 1
                if mode == "backslash":
                    ci += 1
                else:
                    ci -= 1

            return buf

        diagonals = []

        backward_diagonals = (make_diagonal(0, c) for c in range(len(cols)))
        more_backward_diagonals = (make_diagonal(r, 0) for r in range(len(rows)))

        forward_diagonals = (
            make_diagonal(0, c, mode="forwardslash") for c in range(len(cols))
        )
        last_col = len(cols) - 1
        more_forward_diagonals = (
            make_diagonal(r, last_col, mode="forwardslash") for r in range(len(rows))
        )

        candidates = itertools.chain(
            backward_diagonals,
            more_backward_diagonals,
            forward_diagonals,
            more_forward_diagonals,
        )

        diagonals = [c for c in candidates if len(c) >= len(target)]

        found_rows = 0
        for i, row in enumerate(rows):
            occurrences = pat.findall(row)
            found_rows += len(occurrences)

        found_cols = 0
        for i, col in enumerate(cols):
            occurrences = pat.findall(col)
            found_cols += len(occurrences)

        found_diagonals = 0
        for i, diagonal in enumerate(diagonals):
            occurrences = pat.findall(diagonal)
            found_diagonals += len(occurrences)

        print(rows, cols, diagonals)

        return found_rows + found_cols + found_diagonals


def day4_part2():
    return day4()


print(day4_part2())
