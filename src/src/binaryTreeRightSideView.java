import java.util.ArrayList;
import java.util.List;

public class binaryTreeRightSideView {
    // bst트리의 오른쪽 노드들을 나열하는 문제이다.
    // preorder 방식으로 우선 조회하고 해당 depth에 값이 없을시에만 그다음 조회에서 저장되도록 하였다.

    List<Integer> ans=new ArrayList<>();
    public List<Integer> rightSideView(TreeNode root) {

        if(root ==null){
            return ans;
        }
        getRightedNode(root,0);
        System.out.println(ans);

        return ans;
    }
    public void getRightedNode(TreeNode root, int depth){
        TreeNode tmp;               //right 비교시에  root 노드 재할당하면 left때 오류 되므로 tmp 사용

        System.out.println(root.val);
        if(root!=null && ans.size()<=depth){
            ans.add(root.val);
        }

        if(root.right!=null){
            tmp=root.right;
            getRightedNode(tmp,depth+1);
        }

        if(root.left!=null){
            tmp=root.left;
            getRightedNode(tmp,depth+1);
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
