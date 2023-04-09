class Solution(object):
    def removeElement(self, nums, val):

        i = 0
        for element in nums:
            if element != val:
                nums[i] = element
                i += 1

        return i