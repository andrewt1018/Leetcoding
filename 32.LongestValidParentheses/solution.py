# https://leetcode.com/problems/longest-valid-parentheses/submissions/
# Naive solution by checking the longest valid substring for each specific '(' char
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        l = len(s)
        for i in range(l):
            char = s[i]
            if char == ')' or s == l - 1:
                continue
            if longest >= l - i:
                break
            counter = 1
            pairs = 1   # Counting the pairs of parentheses, also used to check validity
            no_end = True
            for j in range(i + 1, l):
                if s[j] == '(':
                    pairs += 1
                else:
                    pairs -= 1
                    no_end = False
                counter += 1
                if pairs == 0:
                    if counter > longest:
                        longest = counter
                if pairs < 0:
                    break
            if longest == 0 and no_end:
                return 0
        return longest



