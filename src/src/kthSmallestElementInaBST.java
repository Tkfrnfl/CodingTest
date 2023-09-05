import java.util.ArrayList;

public class kthSmallestElementInaBST {
    //bst구조에서 k번째 작은 원소를 찾아내는 문제이다.
    //bst조건에 맞추어 In order 조회하여 오름차순으로 배열에 저장한후 k번째 값을 반환하였다.
    ArrayList<Integer> arr= new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        inOrder(root,k);

        return arr.get(k-1);
    }
    public void inOrder(TreeNode root, int k){
        TreeNode tmp;

        if (root.left != null) {
            tmp = root.left;
            inOrder(tmp, k);
        }
        arr.add(root.val);
        if (root.right != null) {
            tmp = root.right;
            inOrder(tmp, k);
        }
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