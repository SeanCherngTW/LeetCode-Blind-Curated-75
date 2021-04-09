class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = a & b
            a = a ^ b  # a + b without considering carry
            b = carry << 1
        return a
