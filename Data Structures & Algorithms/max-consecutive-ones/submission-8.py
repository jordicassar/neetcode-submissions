class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # [1,1,0,1,1,1] -> 3 
        # [1,0,1,1,0,1] -> 2

        # intiliaze a count variable
        count = 0
        # initiliaze a max variable
        max_var = 0
        # iterate through nums list
        for num in nums:
            # check to see if num equals 1
            if num == 1:
                # increment count by 1
                count += 1
                # check to see if count is greater than max variable
                if count > max_var:
                    max_var = count

            # else count equals nothing
            else:
                count = 0

        # return max variable
        return max_var