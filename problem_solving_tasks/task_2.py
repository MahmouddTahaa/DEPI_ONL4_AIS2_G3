from typing import List, Optional


# 1️⃣ [Problem 1](https://leetcode.com/problems/two-sum/description/)


# brute force solution:
# quadratic time complexity O(n^2) where n is the length of the list
# constant space complexity O(1)
def two_sum_quadratic(nums: list, target: int) -> List[int]:
    range_nums: range = range(len(nums))

    for i in range_nums:
        for j in range_nums:
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
    return []


# optimal solution:
# linear time complexity i.e. O(n) where n is the length of the list
# linear space complexity i.e. O(n) due to the `num_dict` dictionary
def two_sum_linear(nums: list, target: int) -> List[int]:
    num_dict: dict = {}

    for i, num in enumerate(nums):
        target_complement: int = target - num
        if target_complement in num_dict:
            return [num_dict[target_complement], i]

        num_dict[num] = i

    return []


######################################################################################


# 2️⃣ [Problem 2](https://leetcode.com/problems/add-two-numbers/description/)


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        lst = []
        curr = self
        while curr:
            lst.append(str(curr.val))
            curr = curr.next
        return " -> ".join(lst)


# time complexity linear* = O(2n + 2m + k) = O(n + m + k) where len(l1) = n, len(l2) = m, len(sum) = k
# sapce complexity O(n + m + k)
class Solution:
    def traverse(self, ll):
        lst = []
        while ll:
            lst.append(ll.val)
            ll = ll.next
        return lst

    def add_two_numbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:

        list1 = self.traverse(l1)[::-1]
        list2 = self.traverse(l2)[::-1]

        val1 = int("".join(map(str, list1)))
        val2 = int("".join(map(str, list2)))
        total = val1 + val2

        dummy = ListNode()
        curr = dummy

        for digit in str(total)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next


# test case: raw( l1 + l2 ) = 807, final res = 7 -> 0 -> 8
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
print(s.add_two_numbers(l1, l2))
