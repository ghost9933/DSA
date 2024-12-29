class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        zCount = 0  # Count of zeros in the current window
        s = []  # Stack to store indices of zeros (no longer needed)
        op = -1  # Left boundary of the window (initialized to -1 for clarity)
        ans = 0  # Max subarray length
        i = 0  # Pointer to traverse the array

        while i < len(nums):
            # Increment zero count if the current element is zero
            if nums[i] == 0:
                zCount += 1
                s.append(i)  # Track the index of the zero (not necessary)

            # Shrink the window if more than one zero
            if zCount > 1:
                # Instead of using the stack, move the left boundary
                op = s.pop(0)  # Remove the first zero index
                zCount -= 1  # Adjust the zero count
            
            # Calculate the max subarray length
            # Subtract 1 from (i - op) to exclude one zero
            ans = max(ans, i - op - 1)

            i += 1

        # No need for a final adjustment (e.g., `ans -= 1`) if logic is correct
        return ans
