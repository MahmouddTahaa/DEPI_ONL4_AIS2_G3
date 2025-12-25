# 1️⃣ [Problem 1](https://www.codewars.com/kata/51c8991dee245d7ddf00000e)
def reversed_words(s: str) -> str:
    reversed_sent: str = " ".join(s.split()[::-1])

    return reversed_sent


######################################################################################


# 2️⃣ [Problem 2](https://www.codewars.com/kata/53af2b8861023f1d88000832)
def are_you_playing_banjo(name: str) -> str:
    first_char: str = name[0].lower()
    plays_banjo: bool = first_char == "r"

    if plays_banjo:
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
