"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

"""

"""
NOTES:
- Each closing parantheses should match with the latest UNUSED opening one.
- Cross out pairs that have already been used up.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        opens = ("([{")
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        unusedOpens = []

        for bracket in s:
            # Is it open?
            if bracket in opens:
                unusedOpens.append(bracket)
            
            # Closed bracket
            else:
                matchingOpen = closeToOpen[bracket]
                if len(unusedOpens) > 0 and matchingOpen == unusedOpens[-1]:
                    unusedOpens.pop()
                else:
                    return False
        
        return len(unusedOpens) == 0