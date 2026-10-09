class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minimum_size = 21485541
        for s in strs:
            if len(s) < minimum_size:
                minimum_size = len(s)
        print(f"minimum size is {minimum_size}")
        if minimum_size == 0:
            return ""
        prefix = []
        for letter in range(minimum_size):
            for string in strs:
                if len(prefix) < letter+1:
                    prefix.append(string[letter])
                elif prefix[letter] != string[letter]:
                    if len(prefix) == 0:
                        return ""
                    prefix.pop()
                    return "".join(prefix)

        return "".join(prefix)
if __name__ == "__main__":
    s = Solution()
    a = s.longestCommonPrefix(strs = ["flower","flow","flight"])
    print(a)