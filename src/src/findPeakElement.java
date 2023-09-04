public class findPeakElement {
    // 주어진 배열에서 특정요소의 인접값이 특정요소보다 작으면 peak이라 하고 그 peak을 찾는 문제이다.
    // peak의 아무 인덱스나 반환하면 되고, 이전요소보다 다음요소가 작을때 peak을 만족하므로 그러한 요소를 탐색한다.
    public int findPeakElement(int[] nums) {
        int ans=0;
        int tmp=-2147483648;
        for(int i=0; i<nums.length;i++){
            if(nums[i]<tmp){
                ans=i;
                return i-1;
            }
            else {
                tmp=nums[i];
            }
            if(i==nums.length-1){
                ans=i;
            }
        }
        return ans;
    }
}
