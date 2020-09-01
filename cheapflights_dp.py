class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        """
            DP
        """
        dp = [[float('inf') for _ in range(n)] for _ in range(K + 2)]
    
                
        dp[0][src] = 0
        for k in range(1, K + 2):
            dp[k][src] = 0
            for u, v, cost in flights:
                dp[k][v] = min(dp[k][v], dp[k - 1][u] + cost) # relax

        return dp[K + 1][dst] if dp[K + 1][dst] != float('inf') else -1