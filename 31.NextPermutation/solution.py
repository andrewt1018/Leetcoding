# https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Check, starting from the back, up until which element is sorted backwards,
        # then replace the last element (i.e smallest element in backwards sorted subset)
        # with the next element that isn't sorted, then sort the backwards sorted subset
        l = len(nums)
        if l == 0 or l == 1:
            return
        prev = l - 1
        current = l - 2
        backwards = True
        while current >= 0:
            if nums[current] < nums[prev]:
                backwards = False
                break
            prev = current
            current -= 1
        if backwards:
            nums.sort()
            return

        # find the smallest element larger than current
        swap = current + 1
        while swap < l and nums[swap] > nums[current]:
            swap += 1
        swap -= 1
        temp = nums[swap]
        nums[swap] = nums[current]
        nums[current] = temp
        nums[current + 1:] = sorted(nums[current + 1:])
        
