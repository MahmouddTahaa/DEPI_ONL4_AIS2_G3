from typing import List


# 1️⃣ (https://leetcode.com/problems/search-insert-position/description/)


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left


######################################################################################

# 2️⃣ (https://leetcode.com/problems/basic-calculator-ii/description/)


def calculate(s: str) -> int:
    stack = []
    current_number = 0
    operation = "+"

    for i, char in enumerate(s):
        if char.isdigit():
            current_number = current_number * 10 + int(char)

        if char in "+-*/" or i == len(s) - 1:
            if operation == "+":
                stack.append(current_number)
            elif operation == "-":
                stack.append(-current_number)
            elif operation == "*":
                stack.append(stack.pop() * current_number)
            elif operation == "/":
                top = stack.pop()
                if top < 0:
                    stack.append(-(-top // current_number))
                else:
                    stack.append(top // current_number)

            operation = char
            current_number = 0

    return sum(stack)
