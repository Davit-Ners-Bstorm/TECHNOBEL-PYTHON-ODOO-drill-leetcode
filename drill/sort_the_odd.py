"""
SORT ARRAY BY PARITY (sort the odd)
Pattern: Arrays / in-place positions

Given a list of integers, sort ONLY the odd numbers in ascending order
while leaving every even number exactly where it is.

Examples:
    sort_odd([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]
    sort_odd([5, 3, 1, 8, 0])    -> [1, 3, 5, 8, 0]
    sort_odd([2, 4, 6])          -> [2, 4, 6]

Walkthrough of the first example:
    odd positions hold 5, 3, 1 (indices 0, 1, 4)
    sorted odds are 1, 3, 5
    drop them back into the same odd positions -> [1, 3, 2, 8, 5, 4]

Think about: collect the odd values, sort them, then place them back
into the slots that originally held an odd value. The even values
never move.
"""

from testkit import check, report


def sort_odd(nums):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("mixed", sort_odd([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
    check("ends with even", sort_odd([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
    check("all even", sort_odd([2, 4, 6]), [2, 4, 6])
    check("all odd", sort_odd([9, 7, 5, 3]), [3, 5, 7, 9])
    check("empty", sort_odd([]), [])
    report()
