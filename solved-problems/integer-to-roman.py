POSSIBLE_CHARS = ["I", "V", "X", "L", "C", "D", "M", "J"]

class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)

        i = len(num) - 1

        reversed_roman = []
        while i > -1:
            curr_algarism = num[i]
            romano_atual = converte_romano((len(num) - 1) - i, curr_algarism)
            reversed_roman.append(romano_atual)
            i -= 1

        reversed_roman.reverse()
        return "".join(reversed_roman)

    
def converte_romano(potencia_dez: int, algarismo: str):
    posicao = 2*potencia_dez
    
    match algarismo:
        case "0":
            return ""
        case "1":
            return POSSIBLE_CHARS[posicao]
        case "2":
            return POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao]
        case "3":
            return POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao]
        case "4":
            return POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao+1]
        case "5":
            return POSSIBLE_CHARS[posicao+1]
        case "6":
            return POSSIBLE_CHARS[posicao+1]+POSSIBLE_CHARS[posicao]
        case "7":
            return POSSIBLE_CHARS[posicao+1]+POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao]
        case "8":
            return POSSIBLE_CHARS[posicao+1]+POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao]
        case "9":
            return POSSIBLE_CHARS[posicao]+POSSIBLE_CHARS[posicao+2]
    

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(num = 4785))