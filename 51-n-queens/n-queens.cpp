class Solution {
public:
vector<vector<string>>res;
void countValid(int i,int n,vector<vector<char>>&board)
{
    if(i==n)
    {  
        vector<string>temp;
        for(int x=0;x<n;x++)
        {
          string row(board[x].begin(),board[x].end());
          temp.push_back(row);
        }
        res.push_back(temp);
        return;
    }

        for(int j=0;j<n;j++)
        {
            int l=i-1,r=j,f=0;
            while(l>=0)
            {
                if(board[l][r]=='Q')
                {
                    f=1;
                    break;
                }
                l--;

            }
            if(f==1)
            continue;
        
         l=i-1,r=j-1;
        while(l>=0 && r>=0)
        {
            if(board[l][r]=='Q')
            {
                f=1;
                break;
            }
            l--;
            r--;
        }
        if(f==1)
        continue;
        l=i-1;
        r=j+1;
        while(l>=0 && r<n)
        {
           if(board[l][r]=='Q'){
           f=1;
           break; 
        }
        l--;
        r++;
    }if(f==1)
    continue;
    board[i][j]='Q';
    countValid(i+1,n,board);
    board[i][j]='.';
    }

}
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<char>>board(n,vector<char>(n,'.'));
         countValid(0,n,board);
         return res;

        
    }
};