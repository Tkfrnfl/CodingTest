public class minimumSizeSubarraySum {
    //하위배열의 합중 target보다 크고 그중에서 가장 짧은 배열의수를 구하는 문제이다.
    //창문슬라이딩을 적용하여 우선 target보다 클때까지 늘린다음 한칸씩 줄이고 그다음 end를 탐색하는 식으로 해결하였다.
    public int minSubArrayLen(int target, int[] nums) {
        int ans=999999;
        int start=0;
        int end=0;
        int sum=0;

        while (end<nums.length){
            sum+=nums[end];

            while (sum>=target){
                sum-=nums[start];
                ans=Math.min(end-start+1,ans);
                start++;
            }
            end++;
        }
        if(ans==999999){            //못찾을시 0으로
            ans=0;
        }

        return ans;
    }
}
