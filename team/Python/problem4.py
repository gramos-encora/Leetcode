class Solution:
    """
    Solution for Leetcode problem 4
    Longest Substring Without Repeating Characters
    """
    def isMatch(self, s: str, p: str) -> bool:
        """
        Given a string and a pattern, implement regular expressions support for '.' and '*'

        Args:
            s: str: String with only English letters.
            p: string: Pattern which contains English letters, '.' and '*'.
        Returns: 
            bool: True if the pattern match else False
        """
        n, m = len(s), len(p)
        # Filling matrix with n+1 rows and m+1 cols
        memory = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        # Base Case
        memory[0][0] = True

        for i in range(n+1):
            for j in range(1, m + 1):
                # If there is a * in pattern
                if p[j-1] == '*':
                    # Option 1: Ignore previous character
                    ignorePattern = (j >= 2 and memory[i][j - 2])

                    # Option 2: If the previous character match with s or .
                    repeatChar = (i > 0 and j >= 2 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and memory[i - 1][j])

                    memory[i][j] = ignorePattern or repeatChar
                else:
                    # Verify if the character with s and p match with current s char or .
                    charMatch = (i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'))

                    # Validating conditions
                    memory[i][j] = i > 0 and memory[i - 1][j - 1] and charMatch
        return memory[n][m]
