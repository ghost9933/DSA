class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        free=[0]
        hold=[-prices[0]]
        # free[0]=0

        for i in range(1,len(prices)):
            hold.append(max(hold[i-1],free[i-1]-prices[i]))
            free.append(max(free[i-1],hold[i-1]+prices[i]-fee))
        print(free)
        return free[-1]

            