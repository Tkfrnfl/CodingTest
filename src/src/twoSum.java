import java.util.HashMap;
import java.util.Map;

public class twoSum {
    // 주어진 배열에서 수 2개를 골라 그 합이 target인 인덱스를 리턴하는 문제이다.
    // num배열을 순회하면서 target과의 차 만큼 해쉬테이블에 저장하고 그다음 배열값중에 해쉬테이블에 있는지 여부를 살펴본다.
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> diff=new HashMap<>();
        int[] ans=new int[2];
        for(int i=0;i<nums.length;i++){
            if(diff.get(nums[i])!=null){
                ans[0]=i;
                ans[1]=diff.get(nums[i]);
                break;
            }
            else{
                diff.put(target-nums[i],i);
            }


        }
        return ans;
    }
}
