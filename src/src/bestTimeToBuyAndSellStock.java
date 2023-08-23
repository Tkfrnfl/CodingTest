public class bestTimeToBuyAndSellStock {
    // 시간순으로 주어진 주가 가격 배열 값에서 가장 큰 이윤을 구하는 문제이다
    // 배열을 역순으로 보면서 가장 큰값을 계속 업데이트하고 만약 이보다 작을시 이윤값을 저장하여 최대값을 얻어낸다.
    public int maxProfit(int[] prices) {

        int ans=0;
        int maxPrice=0;
        for(int i=0;i<prices.length;i++){
            if(prices[prices.length-i-1]>maxPrice){
                maxPrice=prices[prices.length-i-1];
            }
            else {
                ans=Math.max(ans,maxPrice-prices[prices.length-i-1]);
            }
        }
        return ans;
    }
}
