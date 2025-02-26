class Solution:
    """
    Solution fo Leetcode problem 3
    Longest Substring Without Repeating Characters
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the longest substring without repeated characters
        
        Args:
            s: str: String with only English letters, symbols and spaces.
        
        Returns:
            int: The longest length of the substring
        """

        # Dictionary where all the characters will be saved, it works to track the repeated characters
        seen = {}
        left = 0
        maxS = 0
        # Start traversing the array with a window using left and right pointer
        for right in range(len(s)):
            # In case the character has not been seen
            if s[right] not in seen:
                # Comparing the sizes of the window and saving the bigger one
                maxS= max(maxS,(right - left +1))
            else:
                # In case the left pointer is bigger than the right one the window will be reestablished
                if seen[s[right]] < left:
                    maxS = max(maxS,(right- left + 1))
                else:
                    left = seen[s[right]] + 1
            # Save the seen value in the dictionary
            seen[s[right]] = right
        return maxS
