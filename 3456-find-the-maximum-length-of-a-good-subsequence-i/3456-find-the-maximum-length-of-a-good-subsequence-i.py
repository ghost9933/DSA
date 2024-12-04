class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        #  for any fgiven elemnt i have two options to include it or to exclude it
        from collections import defaultdict

        # Step 1: Map unique elements to indices
        unique_nums = list(set(nums))
        num_to_index = {num: idx for idx, num in enumerate(unique_nums)}
        index_to_num = {idx: num for idx, num in enumerate(unique_nums)}
        num_unique = len(unique_nums)

        # Step 2: Initialize DP table
        # dp[l][c] = max length ending with l having c changes
        dp = [[0] * (k + 1) for _ in range(num_unique)]

        for num in nums:
            current_idx = num_to_index[num]
            # Make a copy of dp to iterate over
            dp_copy = [row[:] for row in dp]
            # Iterate over all possible previous last elements
            for prev_idx in range(num_unique):
                for c in range(k + 1):
                    if dp_copy[prev_idx][c] == 0:
                        continue
                    if index_to_num[prev_idx] == num:
                        # Same as previous, no change
                        if dp[prev_idx][c] < dp_copy[prev_idx][c] + 1:
                            dp[prev_idx][c] = dp_copy[prev_idx][c] + 1
                    else:
                        # Different from previous, increase change count
                        if c + 1 <= k:
                            if dp[current_idx][c + 1] < dp_copy[prev_idx][c] + 1:
                                dp[current_idx][c + 1] = dp_copy[prev_idx][c] + 1
            # Also, start a new subsequence with the current num
            if dp[current_idx][0] < 1:
                dp[current_idx][0] = 1

        # Step 3: Find the maximum value in the DP table
        max_length = 0
        for l in range(num_unique):
            for c in range(k + 1):
                if dp[l][c] > max_length:
                    max_length = dp[l][c]
        return max_length

