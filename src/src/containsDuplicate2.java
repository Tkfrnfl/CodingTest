import java.util.HashMap;
import java.util.Map;

public class containsDuplicate2 {
    //주어진 배열에서 같은 값을 가진 값을 찾는문제이다. 이때 두 값의 index 차이가 target보다 작아야한다.
    // 배열을 순회하면서 (배열 값,index값)으로 해쉬테이블에 저장한 후 다음 원소를 탐색할때마다 비교해준다.
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> table=new HashMap<>();
        boolean ans=false;

        for(int i=0;i<nums.length;i++){
            if(table.get(nums[i])!=null){
                if(Math.abs(i-table.get(nums[i]))<=k){
                    return true;
                }
            }
            table.put(nums[i],i);


        }
        return ans;
    }
}
