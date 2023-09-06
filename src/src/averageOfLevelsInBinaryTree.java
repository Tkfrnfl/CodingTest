import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class averageOfLevelsInBinaryTree {
        //bst를 순회하며 각 depth의 평균값을 구하는 문제이다.
        //preOrder방식으로 순회하며 각 노드의 depth별 총합, 개수를 저장해두고 마지막에 리스트에 담아주어 반환하였다.

       List<Double> answer =new ArrayList<>();

        double[] ans= new double[10000];
        List<Integer> count= new ArrayList<>();

        int countDepth=0;
        public List<Double> averageOfLevels(TreeNode root) {
            Arrays.fill(ans,-2147483648);
            if(root==null){

                return  answer;
            }
            itinerateNode(root,0);

            for(int i=0;i<countDepth+1;i++){
                answer.add(ans[i]/count.get(i));
            }

            return answer;
        }
        public void itinerateNode(TreeNode root,int depth){
            TreeNode tmp;
            countDepth=Math.max(countDepth,depth);
            double rootVal= root.val;
            if(ans[depth]==-2147483648){
                ans[depth]=rootVal;
                count.add(1);
            }else {
                count.set(depth,count.get(depth)+1);
               // double avg=(ans[depth]+rootVal)/count.get(depth);
                ans[depth]=ans[depth]+rootVal;
            }

            if(root.left!=null){
                tmp=root.left;
                itinerateNode(tmp,depth+1);
            }
            if(root.right!=null){
                tmp=root.right;
                itinerateNode(tmp,depth+1);
            }
        }


      public class TreeNode {
      int val;
      TreeNode right;
      TreeNode left;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
         this.right = right;
      }
  }
}
