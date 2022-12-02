import os
import sys

sys.path.insert(0, "./utils/py")
import utils


measure_time = utils.stopwatch()


@measure_time
def parse(lines):
    res = [line.strip() for line in lines]

    return res


results = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

results2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


# PART 1
@measure_time
def solve1(data):
    res = 0

    for line in data:
        res += results[line]

    return res


# PART 2
@measure_time
def solve2(data):
    res = 0

    for line in data:
        res += results2[line]

    return res


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    data = parse(open(os.path.join(__location__, "input.txt")).readlines())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
