import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        left1, right1 = 0, len(nums1)-1
        left2, right2 = 0, len(nums2)-1

        #while (right1-left1)>1 and (right2-left2)>1:
        while left1 != right1 and left2 != right2:
            mid1 = (left1+right1) // 2
            mid2 = (left2+right2) // 2

            print(f"middle indexes: {mid1} and {mid2}")

            mid1_value = nums1[mid1]
            mid2_value = nums2[mid2]

            print(f"middle values: {mid1_value} and {mid2_value}")

            #comparing the values so we can discard the part that we want

            if mid1_value < mid2_value:
                left1 = mid1
                right2 = mid2
            else:
                right1 = mid1
                left2 = mid2

        if left1 == right1:
            mid1 = left1
            mid2 = (left2 + right2 + 1)/2
            if mid2%1 != 0:


        else: #left2 == right2

def find_median_list_plus1(element: int, nums: list[int], left_limit: int, right_limit: int):
    insertion_index = bisect.bisect_left(nums, element, lo=left_limit, hi=right_limit)

    if right_limit - left_limit % 2 == 0: #será impar e terá mediana exata
        old_median_index = (right_limit - left_limit) // 2
        if old_median_index > insertion_index:
            new_median = nums[old_median_index + 1]
        
if __name__ == "__main__":
    s = Solution()
    s.findMedianSortedArrays(nums1 = [4, 5, 6], nums2 = [1, 2, 3])