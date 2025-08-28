class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int profit = 0; 
        int i = 0, j = 1;
        while (j < n) {
            int buyPrice = prices[i];
            int sellPrice = prices[j];
            if (sellPrice > buyPrice) {
                profit += sellPrice - buyPrice; // sell the stock.
                                                // note that if the prices are 1,2,3
                                                // we get a profit of 2 whether or not we buy on day 2.
                i = j;
            } else {
                i = j;                          // we get a better buy price 
                                                // by not buying on the initial day
            }
            ++j;
        }
        return profit;
    }
}
