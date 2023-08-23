import java.util.Arrays;

public class majorityElement {
    public int majorityElement(int[] nums) {
        //과반수 요소를 찾는문제
        // 정렬한후에 요소별로 개수 체크하면서 과반수 될시 ans 리턴
        Arrays.sort(nums);
        int count =1;
        int before=nums[0];
        int ans=nums[0];

        for(int i =1; i<nums.length;i++){
            if(before==nums[i]){
                count++;
                if(count>(nums.length/2)){
                   ans= nums[i];
                   break;
                }
            }
            else {
                count=1;
                before=nums[i];
            }
        }
        return  ans;
    }
}
