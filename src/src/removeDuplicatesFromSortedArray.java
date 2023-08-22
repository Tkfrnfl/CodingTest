import java.util.Arrays;

public class removeDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        int before=nums[0];
        int ans=1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]==before){
                nums[i]=999;
            }
            else{
                before=nums[i];
                ans++;
            }
        }

        Arrays.sort(nums);
        return  ans;
    }
}
