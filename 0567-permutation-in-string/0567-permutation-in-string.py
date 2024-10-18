class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Create a frequency map for s1
        map1 = {}
        for char in s1:
            map1[char] = map1.get(char, 0) + 1
        
        # Initialize a frequency map for the current window in s2
        map2 = {}
        window_size = len(s1)
        
        for i in range(len(s2)):
            # Add the current character to the window
            char = s2[i]
            map2[char] = map2.get(char, 0) + 1
            
            # Remove the leftmost character if we've hit the window size
            if i >= window_size:
                left_char = s2[i - window_size]
                if map2[left_char] == 1:
                    del map2[left_char]
                else:
                    map2[left_char] -= 1
            
            # Check if the two maps are equal
            if map1 == map2:
                return True
        
        return False
