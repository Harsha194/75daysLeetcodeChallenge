class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf') 
        if target not in words:
            return -1
        for i, word in enumerate(words):
            if word == target:  
                d1 = abs(i - startIndex)
                d2 = n - d1
                current_closest = min(d1, d2)
                if current_closest < min_dist:
                    min_dist = current_closest
                    
        return min_dist