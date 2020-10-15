# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a , b = 0, 0
        for i in reversed(cost):
            a,b = min(a,b)+i, a
        return min(a,b)