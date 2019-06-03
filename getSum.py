'''
Quest:
    Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

    Example 1:
    Input: a = 1, b = 2
    Output: 3

    Example 2:
    Input: a = -2, b = 3
    Output: 1

Solution:
    bitwise operator
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF # 32 bits integer max
        mask = 0xFFFFFFFF # mask to get last 32 bits

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


test = Solution()
print(test.getSum(-1, -1))