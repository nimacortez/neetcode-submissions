class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        map = []
        for num in nums:
            if num == val:
                continue
            map.append(num)
        for i in range(len(map)):
            nums[i] = map[i]
        return len(map)