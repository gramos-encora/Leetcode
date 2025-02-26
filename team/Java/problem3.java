/*
 Solution for Leetcode problem 3
 Longest Substring without Repeating Characters
*
class Solution {
  /*
   Find the longest substring without repeated characters
   
   Args:
       s: str: String with only English letters, symbols and spaces.
   
   Returns:
       int: The longest length of the substring
  */
  public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> seen = new HashMap();
    Integer left = 0;
    Integer maxS = 0;
    for(int right = 0; right < s.length(); right++) {
      char rightChar = s.charAt(right)
      if (!seen.containsKey(rightChar)){
        maxS = Math.max(maxS, (right - left + 1));
      } else {
        if (seen.get(rightChar) < left) {
          maxS = Math.max(maxS, (right - left + 1));
        } else {
          left = seen.get(right) + 1;
        }
      }
      seen.put(rightChar, right);
    }
    return maxS;
  }
}
