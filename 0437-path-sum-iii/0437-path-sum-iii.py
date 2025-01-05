from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            # Calculate current sum and check for paths ending at this node
            curr_sum += node.val
            path_count = prefix_sum[curr_sum - targetSum]
            
            # Update prefix sums with the current sum
            prefix_sum[curr_sum] += 1
            
            # Recursively check left and right subtrees
            path_count += dfs(node.left, curr_sum)
            path_count += dfs(node.right, curr_sum)
            
            # Backtrack: remove the current sum from prefix_sum
            prefix_sum[curr_sum] -= 1
            
            return path_count
        
        # Initialize prefix sum dictionary
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # Base case: one way to achieve sum 0
        
        return dfs(root, 0)
