class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let sorted = strs.map((str) => str.split("").sort().join(""))
        let map = {}; 
        for (let i = 0; i < strs.length; i++) {
            if (!map[sorted[i]]) {
                map[sorted[i]] = [strs[i]]; 
            } else {
                map[sorted[i]].push(strs[i]);
            }
        } return Object.values(map);
    }
}