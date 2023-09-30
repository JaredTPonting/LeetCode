class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        sub = []
        for i in s:
            if i in sub:
                # store the length of sub and delete characters of sub till the duplicate
                ret = ret if len(sub) < ret else len(sub)
                while sub[0] != i:
                    del sub[0]
                del sub[0]
                sub.append(i)
            else:
                sub.append(i)
                ret = ret if len(sub) < ret else len(sub)
        return ret

j=Solution()
print(j.lengthOfLongestSubstring(s=' '))