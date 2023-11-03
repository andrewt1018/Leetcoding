# https://leetcode.com/problems/longest-valid-parentheses/submissions/
# Uses a stack and appends every character unless it is a ')' and the top of the stack is a '('
from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        length = 0
        l = len(s)
        for i in range(l):
            # Push all '(' characters to the stack
            if s[i] == '(':
                stack.append(i)
                length += 1
                continue
            # Skip if stack is empty
            if length == 0 or s[stack[length - 1]] != '(':
                stack.append(i)
                length += 1
                continue
            # Remove the '(' on the top of the stack because it has a pair
            stack.pop()
            length -= 1
        if length == 0: # Entire string is valid
            return l
        longest = 0
        stack.appendleft(-1)
        stack.append(l)
        length = len(stack)
        for i in range(length - 1):
            long = stack[i + 1] - stack[i] - 1 
            if long > longest:
                longest = long
        return longest


        



