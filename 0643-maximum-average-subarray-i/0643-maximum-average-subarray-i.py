class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize variables
        current_sum = sum(nums[:k])  # Sum of the first `k` elements
        max_average = current_sum / k  # Initialize max average

        # Sliding window approach
        for i in range(k, len(nums)):
            # Update the sum by sliding the window: subtract the element going out and add the element coming in
            current_sum = current_sum - nums[i - k] + nums[i]
            # Update the max average if the new window's average is larger
            max_average = max(max_average, current_sum / k)

        return max_average
