import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if (not nums1) or (not nums2):
            nums = nums1+nums2
            merged_median_index1 = (len(nums)-1)//2
            merged_median_index2 = (len(nums))//2
            median1 = nums[merged_median_index1]
            median2 = nums[merged_median_index2]
            return (median1+median2)/2

        print("initial lists:")
        print(nums1)
        print(nums2)
        while len(nums1) != 1 and len(nums2) != 1:
            #compare medians
            #remove parts
            #repeat
            median_index1 = (len(nums1))//2
            median_index2 = (len(nums2))//2
            print(f"median indexes calculated: {median_index1}, {median_index2}")

            median_number1 = nums1[median_index1]
            median_number2 = nums2[median_index2]

            print(f"medians calculated: {median_number1}, {median_number2}")

            removable_part = min(median_index1, median_index2)
            print(f"can remove at most {removable_part}")

            if median_number1 > median_number2:
                #discard what is above median1
                #and below median2
                nums1 = nums1[:len(nums1)-removable_part]
                nums2 = nums2[removable_part:]

            elif median_number1 <= median_number2:
                #discard below median1
                #and above median2
                nums1 = nums1[removable_part:]
                nums2 = nums2[:len(nums2)-removable_part]

            print("calculated lists")
            print(nums1)
            print(nums2)

        if len(nums1) > len(nums2):
            #call merge on nums1+median2
            return merged_median(nums1, nums2[0])
        elif len(nums1) < len(nums2):
            #call merge on median1+nums2
            return merged_median(nums2, nums1[0])
        else:
            return (nums1[0]+nums2[0])/2

def merged_median(nums, added_num):
    added_num_index = bisect.bisect_left(nums, added_num)
    print(f"insertion index is {added_num_index}")
    merged_median_index1 = (len(nums))//2
    merged_median_index2 = (len(nums)+1)//2
    print(f"calculated merged medians ind: {merged_median_index1}, {merged_median_index2}")

    if merged_median_index1 < added_num_index:
        merged_median1 = nums[merged_median_index1]
    elif merged_median_index1 == added_num_index:
        merged_median1 = added_num
    elif merged_median_index1 > added_num_index:
        merged_median_index1 -= 1
        merged_median1 = nums[merged_median_index1]
    
    if merged_median_index2 < added_num_index:
        merged_median2 = nums[merged_median_index2]
    elif merged_median_index2 == added_num_index:
        merged_median2 = added_num
    elif merged_median_index2 > added_num_index:
        merged_median_index2 -= 1
        merged_median2 = nums[merged_median_index2]

    return (merged_median1+merged_median2)/2
if __name__ == "__main__":
    s = Solution()
    median = s.findMedianSortedArrays([1, 2], [-1, 3])
    print(median)