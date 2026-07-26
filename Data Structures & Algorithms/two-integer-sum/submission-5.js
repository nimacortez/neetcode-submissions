class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const pairIdx = {};

        for (let i = 0; i < nums.length; i++) {
            const num = nums[i];
            if (target - num in pairIdx) {
                return [pairIdx[target - num], i];
            }
            pairIdx[num] = i;
        }
    }
};
