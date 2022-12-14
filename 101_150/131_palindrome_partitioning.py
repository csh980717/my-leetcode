from typing import List


# https://leetcode.com/problems/palindrome-partitioning/discuss/2540042/Python-Backtracking-Solution-or-O(n*(2n))-Time-or-O(n)-Space
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def partitionHelper(start_idx, partition):
            if start_idx == len(s):
                res.append(partition[:])
                return

            for i in range(start_idx, len(s)):
                if self.is_palindrome(s, start_idx, i):
                    partition.append(s[start_idx : i + 1])
                    partitionHelper(i + 1, partition)
                    partition.pop()

        partitionHelper(0, [])
        return res

    def is_palindrome(self, word, left, right):
        while left < right:
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1

        return True
