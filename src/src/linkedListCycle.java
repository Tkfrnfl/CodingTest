public class linkedListCycle {

    //주어진 리스트노드가 순환인지 아닌지 찾는문제이다.
    // 2칸씩가는 노드, 한칸씩가는 노드를 두고 두 노드가 겹치면 순환, 2칸씩가는 노드가 먼저 tail에 도착하면 비순환이다.
    public boolean hasCycle(ListNode head) {
        boolean ans=false;

        ListNode j1=head;
        ListNode j2=head;

        while (j2!=null&&j2.next!=null){        //j2!=null&&j2.next!=null 순서가 바뀌면 컴파일오류 주의!
            j2=j2.next.next;

            j1=j1.next;
            if(j1.val== j2.val){
                ans=true;
                break;
            }
        }
        return ans;
    }
}
  class ListNode {
      int val;
      ListNode next;
     ListNode(int x) {
         val = x;
          next = null;
      }
  }