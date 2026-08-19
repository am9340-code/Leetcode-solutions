class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        leftSum = []
        rightSum = []

        for i in range(len(nums)):
            
            leftSum.append(sum(nums[ :i]))
            rightSum.append(sum(nums[i+1:]))
            answer.append(abs(leftSum[i] - rightSum[i]))

        return answer       