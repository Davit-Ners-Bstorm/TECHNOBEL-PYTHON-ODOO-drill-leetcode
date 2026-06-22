"""
MAXIMUM SUM OF DISTINCT SUBARRAYS WITH LENGTH K
Pattern: Sliding Window + Set

Given a list of integers and an integer k, look at every contiguous
window of exactly k elements. A window is "valid" only if all k
elements are distinct. Return the largest sum among all valid windows.
If no window of length k has all distinct elements, return 0.

Examples:
    max_distinct_sum([1, 5, 4, 2, 9, 9, 9], 3) -> 15   (window [5,4,2,9]? no, k=3)
        windows of size 3: [1,5,4]=10, [5,4,2]=11, [4,2,9]=15,
        [2,9,9] invalid, [9,9,9] invalid -> best valid = 15
    max_distinct_sum([4, 4, 4], 3) -> 0

Think about: slide a window of fixed size k across the list. Keep a
running sum and a frequency map of what is inside the window. When the
window holds k distinct values, it is a candidate. Add the entering
element, remove the leaving one, each step.
"""

from testkit import check, report


def max_distinct_sum(nums, k):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("best is a later window", max_distinct_sum([1, 5, 4, 2, 9, 9, 9], 3), 15)
    check("no valid window", max_distinct_sum([4, 4, 4], 3), 0)
    check("whole list distinct", max_distinct_sum([1, 2, 3], 3), 6)
    check("k equals one", max_distinct_sum([5, 1, 3], 1), 5)
    check("two valid windows", max_distinct_sum([1, 2, 1, 2, 3], 3), 6)
    report()
