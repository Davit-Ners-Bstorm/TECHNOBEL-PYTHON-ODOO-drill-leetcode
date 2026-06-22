"""
UNIQUE IN ORDER
Pattern: Linear scan (compare to previous)

Given a string or a list, return a list of items with consecutive
duplicates removed, keeping the original order. Only repeats that are
ADJACENT are collapsed; the same value appearing again later stays.

Examples:
    unique_in_order("AAAABBBCCDAABBB") -> ['A','B','C','D','A','B']
    unique_in_order("ABBCcAD")         -> ['A','B','C','c','A','D']
    unique_in_order([1, 2, 2, 3, 3])   -> [1, 2, 3]

Think about: this is NOT "remove all duplicates". You only drop an item
when it equals the one immediately before it. So you just need to
remember the previous item as you walk through.
"""

from testkit import check, report


def unique_in_order(iterable):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("string with runs", unique_in_order("AAAABBBCCDAABBB"),
          ['A', 'B', 'C', 'D', 'A', 'B'])
    check("case sensitive", unique_in_order("ABBCcAD"),
          ['A', 'B', 'C', 'c', 'A', 'D'])
    check("list of ints", unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])
    check("empty", unique_in_order(""), [])
    check("no repeats", unique_in_order("ABC"), ['A', 'B', 'C'])
    report()
