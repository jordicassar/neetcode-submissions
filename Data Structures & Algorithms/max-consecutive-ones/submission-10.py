class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # [1,1,0,1,1,1] -> 3 since there are 3 consecutive 1s
        # [1,0,1,1,0,1] -> 2 since there are 2 consecutive 1s

        # initialize count variable
        count = 0
        # initialize max count variable
        max_count = 0

        # iterate through nums array
        for num in nums:

            # check if num is equal to 1
            if num == 1:
                # update count by 1
                count += 1

            # if not equal to 1 count becomes 0 
            else:
                count = 0
            
             # check to see if count is greater than maxcount
            if count > max_count:
                max_count = count 

        return max_count