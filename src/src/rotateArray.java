public class rotateArray {
    //주어진 nums 배열을 우측으로 k만큼 이동시키는 문제
    // k를 nums의 길이 만큼으로 나눈 나머지만큼 이동시켜서 해결하였다
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        int[] temp=new int[nums.length];

        for(int i=0;i<nums.length;i++){
            int j=i+k;
            if(j>=nums.length){
                j-= nums.length;
            }
            temp[j]=nums[i];
        }
        for(int i=0;i<nums.length;i++){
            nums[i]=temp[i];
        }

    }
}
