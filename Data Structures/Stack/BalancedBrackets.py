class Solution(object):
    def isBalancedBrackets(self, string):
        countA = 0
        countB = 0
        countC = 0
        for elem in string:
            if elem == "(":
                countA += 1
            if elem == ")":
                countA -= 1
            if elem == "{":
                countB += 1
            if elem == "}":
                countB -= 1
            if elem == "[":
                countC += 1
            if elem == "]":
                countC -= 1

        if (countA == 0) and (countB == 0) and (countC == 0):
            return True
        else:
            return False

# Driver Code
brackets = "([])()(())()()"
print(Solution().isBalancedBrackets(brackets))