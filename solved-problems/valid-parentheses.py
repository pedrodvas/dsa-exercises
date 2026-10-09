from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else: #is a closing one
                if not stack:
                    return False
                popped = stack.pop()
                if popped == "(" and i != ")":
                    return False
                if popped == "[" and i != "]":
                    return False
                if popped == "{" and i != "}":
                    return False

        if stack:
            return False
        return True
if __name__ == "__main__":
    s = Solution()
    a = s.isValid("()")
    print(a)