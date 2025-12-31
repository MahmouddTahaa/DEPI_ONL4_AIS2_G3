# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 1️⃣ [Problem 1](https://leetcode.com/problems/roman-to-integer/description/)


def roman_to_integer(s: str) -> int:
    r2i_mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    int_value = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and r2i_mapping[s[i]] < r2i_mapping[s[i + 1]]:
            int_value += r2i_mapping[s[i + 1]] - r2i_mapping[s[i]]
            i += 2
        else:
            int_value += r2i_mapping[s[i]]
            i += 1

    return int_value


print(roman_to_integer("III"))
