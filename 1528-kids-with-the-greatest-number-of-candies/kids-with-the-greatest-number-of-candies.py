class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        answer = []
        for candy in candies:
            answer.append(candy + extraCandies >= maximum)
        return answer
        