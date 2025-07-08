class Solution {
public:
    int dp[1001][101][2];
    int solve(int i,int c, int k,int f,vector<int>&prices,int n)
    {
      if(i==n || c==k)
      return 0;
      if(dp[i][c][f]!=-1)
      return dp[i][c][f];
      if(f==0)
      {
        int buy=solve(i+1,c,k,1,prices,n)-prices[i];
        int not_buy=solve(i+1,c,k,0,prices,n);
       return dp[i][c][f]=  max(buy,not_buy);
      }
      else{
      int sell=solve(i+1,c+1,k,0,prices,n)+prices[i];
      int not_sell=solve(i+1,c,k,1,prices,n);
      return dp[i][c][f]=max(sell,not_sell);
    }
    }
    int maxProfit(int k, vector<int>& prices) {
     int n=prices.size();
     int c=0;
     int f=0;
     memset(dp,-1,sizeof(dp));
     int profit=solve(0,c,k,f,prices,n);
     return profit;

        
    }

    
};