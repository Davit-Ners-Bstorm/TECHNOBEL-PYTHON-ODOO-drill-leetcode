"""
CHALLENGE 21

A promo code is considered "almost symmetric" if it reads the same
forwards and backwards after deleting at most one character. Given a
code, return True if it is already a palindrome or can become one by
removing a single character, otherwise False.

Examples:
    almost_palindrome("abca") -> True   (remove 'b' or 'c')
    almost_palindrome("abc")  -> False

Contract:
Comparison is exact and case-sensitive; do not remove punctuation or
spaces unless using your one deletion. Empty input returns True.

"""

from testkit import check, report


def almost_palindrome(code):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("already palindrome", almost_palindrome("aba"), True)
    check("remove one", almost_palindrome("abca"), True)
    check("cannot fix", almost_palindrome("abc"), False)
    check("empty", almost_palindrome(""), True)
    check("single char", almost_palindrome("a"), True)
    check("two chars", almost_palindrome("ab"), True)
    check("remove first", almost_palindrome("deeee"), True)
    check("needs two removals", almost_palindrome("abcda"), False)
    check('must try deleting right side', almost_palindrome("abbab"), True)
    check('case matters', almost_palindrome("Aaab"), False)
    report()
