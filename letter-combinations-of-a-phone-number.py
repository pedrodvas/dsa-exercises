from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        queue = deque()
        queue.append("")

        return_list = []
        while queue:
            curr_string = queue.popleft()
            next_key = len(curr_string)

            if next_key != len(digits):
                possible_letters = get_letters(digits[next_key])
                for i in possible_letters:
                    queue.append(curr_string+i)
                    print(f"appended {curr_string+i}")
            else:
                return_list.append(curr_string)

        return return_list


def get_letters(key: chr) -> str:
    match key:
        case "2":
            return "abc"
        case "3":
            return "def"
        case "4":
            return "ghi"
        case "5":
            return "jkl"
        case "6":
            return "mno"
        case "7":
            return "pqrs"
        case "8":
            return "tuv"
        case "9":
            return "wxyz"
if __name__ == "__main__":
    s = Solution()
    s.letterCombinations(digits = "23")