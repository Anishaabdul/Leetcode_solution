class Solution:
    def plusOne(self, digits):
        n = ""

        for digit in digits:
            n += str(digit)

        n = int(n) + 1

        result = []

        for digit in str(n):
            result.append(int(digit))

        return result