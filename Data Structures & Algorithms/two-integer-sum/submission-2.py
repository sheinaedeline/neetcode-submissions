class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dict to store remainder number to sum up into the target
        remainder_dict = dict()

        # If remainder exists in dict, stop loop
        for i in range(len(nums)):
            remainder = target - nums[i]
            # Found pair
            if remainder not in remainder_dict:
                return sorted([i, remainder_dict[remainder]])
            remainder_dict[nums[i]] = i
        
            