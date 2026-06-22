"""
CHALLENGE 16

A row of storage tanks sits side by side, each described by its wall
height (one unit apart). Choosing two walls forms a container, and the
water it can hold is limited by the shorter wall and the distance between
them. Given the wall heights, return the most water any pair of walls can
hold.

Examples:
    most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49
    most_water([1, 1])                       -> 1

"""

from testkit import check, report


def most_water(heights):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("classic", most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    check("two walls", most_water([1, 1]), 1)
    check("tall ends", most_water([4, 3, 2, 1, 4]), 16)
    check("small dip", most_water([1, 2, 1]), 2)
    check("empty", most_water([]), 0)
    check("single wall", most_water([5]), 0)
    report()
