class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = nums.size()-1; i >=2; i--){
            int tSum = nums[i-1] + nums[i-2];
            if (nums[i] < tSum){
                return nums[i] + tSum;
            }
        }
        return 0;
    }
};
