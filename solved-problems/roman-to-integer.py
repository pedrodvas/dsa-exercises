class Solution:
    def romanToInt(self, s: str) -> int:
        i = len(s) - 1
        total = 0
        total += to_number(s[i])
        i -= 1
        while i > -1:
            if to_number(s[i]) < to_number(s[i+1]):
                total -= to_number(s[i])
            else:
                total += to_number(s[i])
            i -= 1

        return total

def to_number(roman: chr):
    match roman:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000

if __name__ == "__main__":
    s = Solution()
    s.romanToInt(s = "LVIII")