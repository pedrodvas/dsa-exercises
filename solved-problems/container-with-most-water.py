class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height)-1

        maior_volume = 0

        while i < j:
            #processa algo
            volume = calcula_volume([i, height[i]], [j, height[j]])
            if volume > maior_volume:
                maior_volume = volume
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maior_volume


def calcula_volume(parede1: list[int, int], parede2: list[int, int]):
    comprimento = parede2[0] - parede1[0]
    altura = min(parede1[1], parede2[1])

    return altura*comprimento



if __name__ == "__main__":
    s = Solution()
    a = s.maxArea(height = [1,8,6,2,5,4,8,3,7])
    print(a)