class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean rows[][]=new boolean[9][9];
        boolean cols[][]=new boolean[9][9];
        boolean square[][]=new boolean[9][9];

        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j]=='.')
                {
                    continue;
                }
                int n=board[i][j]-'0';
                if(rows[i][n-1])
                {
                    return false;
                }
                else
                {
                    rows[i][n-1]=true;
                }
                if(cols[j][n-1])
                {
                    return false;
                }
                else
                {
                    cols[j][n-1]=true;
                }

                int sq=(i/3)*3+j/3;
                if(square[sq][n-1])
                {
                    return false;
                }
                else
                {
                    square[sq][n-1]=true;
                }
            }
        }

        return true;
    }
}
