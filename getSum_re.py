"""
Quest:
    Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

    Example 1:

    Input: a = 1, b = 2
    Output: 3
    Example 2:

    Input: a = -2, b = 3
    Output: 1

Solution:
    - bitwise operator
    -
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # need to deal with negative value and overflow
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= MAX else ~ (a ^ mask)


test = Solution()
a = -2
b = 3
print(test.getSum(a, b))