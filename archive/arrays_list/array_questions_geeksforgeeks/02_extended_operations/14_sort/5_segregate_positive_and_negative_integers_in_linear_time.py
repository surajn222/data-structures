# TODO: Completed: https://leetcode.com/problems/rearrange-array-elements-by-sign/
# https://leetcode.com/problems/rearrange-array-elements-by-sign/ #Pending
# https://www.techiedelight.com/positive-and-negative-integers-segregate/
# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = []
        neg = []
        for i in range(0, len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])

        # print(pos)
        # print(neg)
        final_arr = []
        len_arr = min(len(pos), len(neg))
        for i in range(0, len_arr):
            final_arr.append(pos[i])
            final_arr.append(neg[i])

        # print(final_arr)
        if len(pos) < len(neg):
            final_arr.append(neg[i:])
        elif len(pos) > len(neg):
            final_arr.append(pos[i:])

        return final_arr