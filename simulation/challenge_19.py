"""
CHALLENGE 19

A museum ticketing system stores edition numbers as Roman numerals and
needs them converted back to ordinary integers. The numerals use the
usual symbols (I=1, V=5, X=10, L=50, C=100, D=500, M=1000) with the
standard subtraction rule (e.g. IV is 4, IX is 9, CM is 900).

Given a valid Roman numeral string, return its integer value.

Examples:
    roman_value("LVIII")   -> 58
    roman_value("MCMXCIV") -> 1994

Contract:
Inputs are valid uppercase Roman numerals from 1 to 3999.
As a local extension, the empty string returns 0.

"""

from testkit import check, report


def roman_value(numeral):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("simple", roman_value("III"), 3)
    check("mixed", roman_value("LVIII"), 58)
    check("subtractions", roman_value("MCMXCIV"), 1994)
    check("four", roman_value("IV"), 4)
    check("nine", roman_value("IX"), 9)
    check("recent year", roman_value("MMXXIV"), 2024)
    check("empty", roman_value(""), 0)
    check('largest canonical numeral', roman_value("MMMCMXCIX"), 3999)
    report()
