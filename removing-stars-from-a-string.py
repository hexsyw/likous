# https://leetcode.cn/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                if len(stack) >= 1 and stack[-1] != "*":
                    stack.pop(-1)
            else:
                stack.append(char)
            
        return "".join(stack)

        

if __name__ == "__main__":
    sol = Solution()
    sol.removeStars("erase*****")
