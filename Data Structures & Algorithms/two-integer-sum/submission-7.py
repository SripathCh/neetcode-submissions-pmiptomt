class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            print(nums[i])
            for j in range(i+1,n):
                print(nums[j])
                if nums[i] + nums[j] == target:
                    return [i,j]

        