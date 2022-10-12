class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        for (int i = nums.length-1; i >= 2; i--) {
            int x = nums[i-1] + nums[i-2];
            if (nums[i] < x)
                {
                    return x + nums[i];
            } 
        }
        return (int) 0;
    }
}
