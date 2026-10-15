"""
CHALLENGE 23

A session tracker reads a stream of single-character event codes and
wants the length of the longest run of consecutive events in which no
event code repeats. Given the string of event codes, return that length.

Examples:
    longest_clean_run("abcabcbb") -> 3   ("abc")
    longest_clean_run("pwwkew")   -> 3   ("wke")

Contract:
Comparison is case-sensitive; spaces also count as event codes.
Empty input returns 0. Events must remain contiguous.

"""

from testkit import check, report


def longest_clean_run(events):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("repeats later", longest_clean_run("abcabcbb"), 3)
    check("all same", longest_clean_run("bbbbb"), 1)
    check("window in middle", longest_clean_run("pwwkew"), 3)
    check("empty", longest_clean_run(""), 0)
    check("two distinct", longest_clean_run("au"), 2)
    check("tricky reset", longest_clean_run("dvdf"), 3)
    check("repeat at ends", longest_clean_run("abba"), 2)
    check('spaces are events', longest_clean_run("a b a"), 3)
    check('case matters', longest_clean_run("aA"), 2)
    report()
