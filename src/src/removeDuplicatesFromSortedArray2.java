import java.util.Arrays;

public class removeDuplicatesFromSortedArray2 {
    // 3개이상 중복된 요소를 제거하는 문제
    // count 수를 체크하여 3개이상 될시 제거하고 아닐시 ans  값을 증가하여 요소개수 체크
    public int removeDuplicates(int[] nums) {
        int before= nums[0];
        int count=0;
        int ans=0;

        for(int i=1; i<nums.length;i++){
            if(before==nums[i]){

                if(count>0){
                    nums[i]=10001;
                }
                else{
                    count++;
                    ans++;
                }
            }
            else {
                count=0;
                before=nums[i];
                ans++;
            }
        }
        Arrays.sort(nums);
        return ans+1;
    }
}
