class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_size = len(nums)    
        for i in range(list_size):
            for j in range(list_size):
                if nums[i] + nums[j] == target and i != j :
                    return[i,j]
      
    
if __name__ =='__main__':
    c =Solution()
    Solution.twoSum(c,[3, 2, 4], 6)