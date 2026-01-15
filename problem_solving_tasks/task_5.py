from typing import List


# 1 reverse words
def reverseWords(s: str) -> str:
    words = s.split()
    return " ".join(words[::-1])


# 2 product except self
def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    prfx = 1
    for i in range(n):
        answer[i] = prfx
        frfx *= nums[i]

    sufx = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= sufx
        sufx *= nums[i]

    return answer
