import heapq

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        # Step 1: Create a frequency map to count occurrences of each element in nums
        freq_map = {}
        for ele in nums:
            freq_map[ele] = 1 + freq_map.get(ele, 0)
        
        # Step 2: Convert the frequency map values into a list to use with a heap
        freq_list = list(freq_map.values())
        heap = []
        
        # Step 3: Push all frequencies into a max-heap (inverted sign for max-heap functionality)
        for freq in freq_list:
            heapq.heappush(heap, -freq)
        print(heap)  # Debugging line to show the heap contents

        # Step 4: Perform the removal process as long as there are at least two frequencies in the heap
        while len(heap) > 1:
            # Pop the two largest frequencies from the heap
            maxi_1 = -(heapq.heappop(heap))
            maxi_2 = -(heapq.heappop(heap))

            # Decrease each of these frequencies by 1, simulating the removal of two elements
            maxi_1 -= 1
            maxi_2 -= 1

            # Push the reduced frequencies back into the heap if they are still non-zero
            if maxi_1 != 0:
                heapq.heappush(heap, -maxi_1)
            if maxi_2 != 0:
                heapq.heappush(heap, -maxi_2)
        
        # Step 5: If there are any frequencies left in the heap, return it as the result
        # Otherwise, return 0 indicating all elements were removed
        if heap:
            return -(heap[0])
        else:
            return 0