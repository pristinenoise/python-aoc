import os
import sys

sys.path.insert(0, "./utils/py")
import utils


measure_time = utils.stopwatch()


@measure_time
def parse(lines):
    res = [line for line in lines]

    return res


# PART 1
@measure_time
def solve1(data):
    res = 0

    return res


# PART 2
@measure_time
def solve2(data):
    res = 0

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
