class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(i):
        # Out of bounds or already visited
            if i < 0 or i >= len(arr) or arr[i] < 0:
                return False
            
            # Found a zero
            if arr[i] == 0:
                return True
            
            # Mark as visited (negate value)
            jump = arr[i]
            arr[i] = -arr[i]   # mark visited
            
            # Explore both directions
            return dfs(i + jump) or dfs(i - jump)
        
        return dfs(start)

        