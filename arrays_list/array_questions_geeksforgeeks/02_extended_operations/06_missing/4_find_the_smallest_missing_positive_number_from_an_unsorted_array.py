



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        i = 0
        while i <= len(nums)-1:
            while i != len(nums)-1 and nums[i+1] == nums[i]:
                i+=1
                continue
            if nums[i] > 0:
                if nums[i] != ans:
                    return ans
                else:
                    ans = ans + 1

            i+=1
        return ans