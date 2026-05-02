class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # ******************HASHMAP SOLUTION*************************

        # dic = {}

        # for i,j in enumerate(nums):
        #     complement = target - j
        #     if complement in dic:
        #         return [dic[complement],i]
        #     dic[j] = i
        
        # **************** TWO POINTERS SOLUTION *********************

        A = []

        for i, num in enumerate(nums):
            A.append([num,i])
        A.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            sum = A[left][0] + A[right][0]
            if sum == target:
                return [min(A[left][1],A[right][1]), max(A[left][1],A[right][1])]
            elif sum > target:
                right -= 1
            else: left += 1
        
        return []
