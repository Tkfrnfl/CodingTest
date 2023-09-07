import java.util.ArrayList;
import java.util.Collections;

public class minimumAbsoluteDifferenceInbst {
    // 주어진 bst에서 어느 노드든 최소의 절대값 차이를 구하는 문제이다.
    //순회를하며 각 노드값을 배열에 담아준후 배열을 정렬하고 배열을 돌며 최소값을 찾았다.

    int ans=100000;
    ArrayList<Integer> arr=new ArrayList<>();
    public int getMinimumDifference(TreeNode root) {
        search(root);
        Collections.sort(arr);

        for(int i=0;i<arr.size()-1;i++){
            ans=Math.min(ans,Math.abs(arr.get(i)-arr.get(i+1)));
        }
        return ans;
    }

    public void search(TreeNode root){
        TreeNode tmp;
        arr.add(root.val);
        if(root.left!=null){
            tmp=root.left;
            search(tmp);
        }
        if(root.right!=null){
            tmp=root.right;
            search(tmp);
        }
    }

      public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
}
