import re

NUMBERS = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}


def part_a():
    sum = 0
    with open("./day_01/day_01.txt") as f:
        lines = f.readlines()

        # for line in lines:
        #     for k, v in NUMBERS.items():
        #         line = line.replace(k, v)
        for line in lines:
            nums = re.findall(r"\d", line)

            if nums:
                sum += int(nums[0] + nums[-1])

    print(sum)


def part_b():
    sum = 0
    with open("./day_01/day_01.txt") as f:
        lines = f.readlines()

    for line in lines:
        for k, v in NUMBERS.items():
            line = line.replace(k, v)

        nums = re.findall(r"\d", line)

        if nums:
            sum += int(nums[0] + nums[-1])

    print(sum)


if __name__ == "__main__":
    part_a()
    part_b()
