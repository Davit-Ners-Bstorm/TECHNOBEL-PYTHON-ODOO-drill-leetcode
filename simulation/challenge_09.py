"""
CHALLENGE 9

An analytics dashboard shows the most viewed product IDs from a stream
of page views. Given the list of viewed product IDs and a number k,
return the k product IDs that appear most often.

To keep the output predictable, sort the result by frequency from
highest to lowest, breaking ties by smaller product ID first.

Examples:
    top_viewed([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
    top_viewed([4, 4, 4, 5, 5, 6, 6, 6, 6], 2) -> [6, 4]

"""

from testkit import check, report


def top_viewed(views, k):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("two most viewed", top_viewed([1, 1, 1, 2, 2, 3], 2), [1, 2])
    check("clear order", top_viewed([4, 4, 4, 5, 5, 6, 6, 6, 6], 2), [6, 4])
    check("single id", top_viewed([1], 1), [1])
    check("tie by value", top_viewed([1, 2], 2), [1, 2])
    check("tie picks smaller", top_viewed([7, 7, 3, 3, 1], 1), [3])
    check("k equals distinct", top_viewed([1, 1, 2, 2, 3], 3), [1, 2, 3])
    check("zero requested with views", top_viewed([1, 1, 2], 0), [])
    check("zero requested", top_viewed([], 0), [])
    report()
