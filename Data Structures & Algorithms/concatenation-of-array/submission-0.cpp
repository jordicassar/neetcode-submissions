class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> numsTwo(2 * n);
        for (int i = 0; i < n; i++) {
            numsTwo[i] = nums[i];
            numsTwo[i + n] = nums[i];
        }
        return numsTwo;
    }
};