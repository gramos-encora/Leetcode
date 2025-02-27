function isMatch(s: string, p: string): boolean {
  /*
  * Solution for Leetcode Problem
  * Regular Expression Matching
  */
  let n: number = s.length
  let m: number = p.length
  let memory: boolean[][] = Array(n + 1).fill(null).map(() => Array(m + 1).fill(false))

  memory[0][0] = true

  for (let j = 1; j <= m; j++) {
    if (p[j - 1] === '*') {
      memory[0][j] = memory[0][j - 2];
    }
  }

  for (let i = 0; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (p[j - 1] == '*') {
        memory[i][j] = memory[i][j - 2] ||
          (i > 0 && (s[i - 1] === p[j - 2] || p[j - 2] === '.') && memory[i - 1][j]);
      } else {
        memory[i][j] = i > 0 && memory[i - 1][j - 1] && (s[i - 1] === p[j - 1] || p[j - 1] === '.');
      }
    }
  }
  return memory[n][m]
}
