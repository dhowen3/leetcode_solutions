// idea : explore all board edges and run dfs to mark all connected cells as 
// needing to stay
// mark everything else as X

class Solution {
    public void bfs(char[][] board, boolean[][] explored, int i, int j, int m, int n) {
        LinkedList<int[]> exploreNext = new LinkedList<int[]>();
        exploreNext.add(new int[] {i,j});
        while (!exploreNext.isEmpty()) {
            int[] current = exploreNext.pop();
            i = current[0];
            j = current[1];
            if (explored[i][j] || board[i][j] == 'X') {
                continue;
            } 
            explored[i][j] = true;
            if (i > 0) {
                exploreNext.add(new int[] {i - 1, j});
            }
            if (i < m - 1) {
                exploreNext.add(new int[] {i + 1, j});
            }
            if (j > 0) {
                exploreNext.add(new int[] {i, j - 1});
            }
            if (j < n - 1) {
                exploreNext.add(new int[] {i, j + 1});
            }
        }
    }

    public void markWithXs(char[][] board, boolean[][] explored, int m, int n) {
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!explored[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    public void solve(char[][] board) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] explored = new boolean[m][n];
        // edges:
        // top 
        for (int j = 0; j < n; ++j) {
            int i = 0;
            bfs(board, explored, i, j, m, n);
        }
        // bottom
        for (int j = 0; j < n; ++j) {
            int i = m - 1;
            bfs(board, explored, i, j, m, n);
        }
        // left
        for (int i = 1; i < m - 1; ++i) {
            int j = 0;
            bfs(board, explored, i, j, m, n);
        }
        // right
        for (int i = 1; i < m - 1; ++i) {
            int j = n - 1;
            bfs(board, explored, i, j, m, n);
        }
        markWithXs(board, explored, m, n);
    }
}
