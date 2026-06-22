"""
SEARCH INSERT POSITION
Pattern: Binary Search

Given a sorted list of distinct integers and a target value, return the
index of the target if it is found. If not, return the index where it
would be inserted to keep the list sorted.

Examples:
    search_insert([1, 3, 5, 6], 5) -> 2
    search_insert([1, 3, 5, 6], 2) -> 1
    search_insert([1, 3, 5, 6], 7) -> 4
    search_insert([1, 3, 5, 6], 0) -> 0

Think about: the list is sorted, so you do not need to scan it all.
Keep a low and a high boundary and halve the search space each step.
Where do low and high end up when the target is not present?
"""

from testkit import check, report


def search_insert(nums, target):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("found in middle", search_insert([1, 3, 5, 6], 5), 2)
    check("insert in middle", search_insert([1, 3, 5, 6], 2), 1)
    check("insert at end", search_insert([1, 3, 5, 6], 7), 4)
    check("insert at start", search_insert([1, 3, 5, 6], 0), 0)
    check("single element found", search_insert([1], 1), 0)
    check("single element after", search_insert([1], 2), 1)
    report()
