class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = 0
        num = x

        while num > 0:
            total += num % 10
            num //= 10

        if x % total == 0:
            return total

        return -1