from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        left = 0
        formed = 0
        required = len(need)

        minLen = float("inf")
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left

                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in need and window[leftChar] < need[leftChar]:
                    formed -= 1

                left += 1

        if minLen == float("inf"):
            return ""

        return s[start:start + minLen]