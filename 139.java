class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean dp[][] = new boolean[n+1][n+1];
        for (int l = 1; l <= n; ++l) { // length of substring being evaluated
            for (int i = 0; i + l <= n; ++i) {
                int j = i + l; // i - start index of substring , j - end (sim.)
                boolean wordInDict = wordDict.contains(s.substring(i,j));
                if (wordInDict) {
                    dp[i][j] = true;
                    continue;
                }
                System.out.println("" + i + " " + j);
                for (int k = 1; k < l; ++k) {
                    if (dp[i][j-l+k] && dp[i+k][j]) {
                        dp[i][j] = true;
                        break;
                    }
                    System.out.println(k);
                }
            }
        }
        return dp[0][n];
    }

}
