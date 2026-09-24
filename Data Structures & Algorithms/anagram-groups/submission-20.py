class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

# create map
# iterate through each string, sort characters of string to form a key
# append original string to the list corresponding to the key
# return all values from hash map 

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        
        return list(res.values())