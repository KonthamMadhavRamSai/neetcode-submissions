class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return "/0"

        encodedmsg = strs[0]

        for i in range(1, len(strs)):

            encodedmsg = encodedmsg + "||" + strs[i]

        return encodedmsg


    def decode(self, s: str) -> List[str]:

        if s == "/0":
            return []

        if s == "":
            return [""]

        decoded = []

        low = 0

        i = 0

        while i < len(s)-1:

            if s[i] == "|" and s[i+1] == "|":

                decoded.append(s[low:i])

                low = i + 2

                i += 1

            i += 1

        decoded.append(s[low:])

        return decoded