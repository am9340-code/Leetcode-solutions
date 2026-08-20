class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []

        for i in range(len(prices)):
            found = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    found = True
                    answer.append(prices[i] - prices[j])
                    break
            if found == False:
                answer.append(prices[i])

        return answer

        