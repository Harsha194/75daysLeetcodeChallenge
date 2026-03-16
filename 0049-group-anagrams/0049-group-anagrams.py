class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for num in strs:
            sorted_list="".join(sorted(num))
            a[sorted_list].append(num)
        return list(a.values())
            
        