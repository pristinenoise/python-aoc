import os
import sys

sys.path.insert(0, "./utils/py")
import utils


measure_time = utils.stopwatch()


@measure_time
def parse(lines):
    elves = []
    elf = []
    for line in lines:
        line = line.strip()
        if not line.strip():
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line))

    elves.append(elf)

    return elves


# PART 1
@measure_time
def solve1(data):
    max_calories = 0
    for elf in data:
        calories = sum(elf)
        max_calories = max(max_calories, calories)

    return max_calories


# PART 2
@measure_time
def solve2(data):
    sorted_elves = sorted([sum(elf) for elf in data], reverse=True)
    top3sum = sum(sorted_elves[0:3])

    return top3sum


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
