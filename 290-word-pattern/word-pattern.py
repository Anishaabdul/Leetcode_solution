class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        dic = {}

        for i in range(len(pattern)):

            if pattern[i] not in dic:

                if words[i] in dic.values():
                    return False

                dic[pattern[i]] = words[i]

            else:
                if dic[pattern[i]] != words[i]:
                    return False

        return True