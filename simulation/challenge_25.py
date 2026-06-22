"""
CHALLENGE 25

A plagiarism checker scans a document for every spot where a window of
text uses the exact same letters (same counts) as a target keyword, in
any order. Given the document text and the keyword, return the starting
indices of every such window.

Return the indices in ascending order.

Examples:
    scramble_spots("cbaebabacd", "abc") -> [0, 6]
    scramble_spots("abab", "ab")        -> [0, 1, 2]

"""

from testkit import check, report


def scramble_spots(text, keyword):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("two spots", scramble_spots("cbaebabacd", "abc"), [0, 6])
    check("overlapping", scramble_spots("abab", "ab"), [0, 1, 2])
    check("no match", scramble_spots("aa", "bb"), [])
    check("empty text", scramble_spots("", "a"), [])
    check("keyword too long", scramble_spots("a", "ab"), [])
    check("single spot", scramble_spots("baa", "aa"), [1])
    report()
