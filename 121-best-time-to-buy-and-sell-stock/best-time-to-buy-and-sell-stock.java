class Solution {
    public int maxProfit(int[] prices) {
        int min=prices[0],max=prices[0],maxProfit=0;
    
            for(int i=1;i<prices.length;i++){
            if(prices[i]<min)
            {
                min=prices[i];
                
            }
            
            int profit=prices[i]-min;
           if(profit>maxProfit)
           {
            maxProfit=profit;
           }
    }
           
        
    return maxProfit;
    }
}