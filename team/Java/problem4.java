import java.util.Arrays;

class Solution {
  /*
   * Solution for Leetcode Problem
   * Regular Expression Matching
   */
  public boolean isMatch(String s, String p) {
    Integer n = s.length();
    Integer m = p.length();
    Boolean[][] memory = new Boolean[n + 1][m + 1];
    for (Boolean[] row : memory) {
      Arrays.fill(row, false);
    }
    memory[0][0] = true;

    for (Integer j = 2; j <= m; j++) {
      if (p.charAt(j - 1) == '*') {
        memory[0][j] = memory[0][j - 2];
      }
    }

    for (Integer i = 1; i <= n; i++) {
      for (Integer j = 1; j <= m; j++) {
        if (p.charAt(j - 1) == '*') {
          memory[i][j] = memory[i][j - 2]
              || (i > 0 && (s.charAt(i - 1) == p.charAt(j - 2) || p.charAt(j - 2) == '.') && memory[i - 1][j]);
        } else {
          memory[i][j] = i > 0 && memory[i - 1][j - 1]
              && (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '.');
        }
      }
    }

    return memory[n][m];
  }
}
