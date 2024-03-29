public class jumpGame {
    //주어진 배열의 값이 점프할수 있는 최대 거리이고, 맨 처음부터 점프하여 끝까지 갈수있는지 묻는 문제이다.
    //각 배열을 조회하면서 max  값을 저장하는데 이때 한칸 씩 이동하면서 최대이동거리가 1씩 줄어듦을 적용한다.
    public boolean canJump(int[] nums) {
        int maxNum=nums[0];
        boolean ans=false;

        if(nums.length==1){             //길이 1인경우 예외처리
            return true;
        }

        for(int i=1;i<nums.length;i++){
            maxNum-=1;                  // 이동거리1씩 줄어듦

            if(maxNum<=-1){             //더이상 이동불가시 종료
                break;
            }
            if(i==nums.length-1){
                return true;
            }

            if(maxNum<nums[i]){
                maxNum=nums[i];
            }

        }
        return ans;
    }
}
