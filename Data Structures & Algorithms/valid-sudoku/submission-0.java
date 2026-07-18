class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] row=new boolean[9][9];
        boolean[][] col=new boolean[9][9];
        boolean[][] sq=new boolean[9][9];

        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
               if(board[i][j]=='.')
               {
                continue;
               } 
               else
               {
                    int c=board[i][j] - '0';
                    if(row[i][c-1]) 
                    {
                        return false;
                    }                
                    else
                    {
                        row[i][c-1]=true;
                    }

                    if(col[j][c-1]) 
                    {
                        return false;
                    }                
                    else
                    {
                        col[j][c-1]=true;
                    }

                    int s=(i/3)*3+j/3;
                    if(sq[s][c-1])
                    {
                        return false;
                    }
                    else
                    {
                        sq[s][c-1]=true;
                    }
               }
            }
        }

        return true;
    }
}
