"""
CHALLENGE 18

A file browser groups uploaded files by the longest leading path they
all share. Given a list of file names, return the longest starting string
that every name begins with. If they share no common start, return the
empty string.

Examples:
    common_start(["flower", "flow", "flight"]) -> "fl"
    common_start(["dog", "racecar", "car"])    -> ""

"""

from testkit import check, report


def common_start(names):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("shared prefix", common_start(["flower", "flow", "flight"]), "fl")
    check("nothing shared", common_start(["dog", "racecar", "car"]), "")
    check("long prefix",
          common_start(["interspecies", "interstellar", "interstate"]),
          "inters")
    check("single name", common_start(["alone"]), "alone")
    check("empty list", common_start([]), "")
    check("identical names", common_start(["same", "same"]), "same")
    check("contains empty", common_start(["abc", ""]), "")
    report()
