/*
 Solution for Leetcode problem 3
 Longest Substring without Repeating Characters
*/
function lengthOfLongestSubstring(s: string): number {
  /*
   Find the longest substring without repeated characters
   
   Args:
       s: str: String with only English letters, symbols and spaces.
   
   Returns:
       int: The longest length of the substring
  */

  let seen: Map<string, number> = new Map<string, number>()
  let left: number = 0
  let maxS: number = 0

  for (const [right, rightChar] of s.split("").entries()) {
    if (!seen.has(rightChar)) {
      maxS = Math.max(maxS, (right - left + 1))
    } else {
      if (seen.get(rightChar)! < left) {
        maxS = Math.max(maxS, (right - left + 1))
      } else {
        left = seen.get(rightChar)! + 1
      }
    }
    seen.set(rightChar, right)
  }
  return maxS
}
