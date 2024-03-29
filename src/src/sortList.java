import java.util.ArrayList;
import java.util.Collections;

public class sortList {
    // 링크드리스트의 값기준으로 정렬하는 문제이다.
    // 분할정복을 사용하려했으나 아이디어가 떠오르지 않아서 배열을 활용하여 해결하였다.


    // *** 분할정복 사용시 keyPoint: tmp.next, tmp.next.next 를 이용하여 링크드리스트를 반으로 나눈다!
    public ListNode sortList(ListNode head) {
        ArrayList<Integer> arr=new ArrayList<>();

        if(head==null){
            return null;
        }

        ListNode temp=head;
        while (temp.next!=null){
            arr.add(temp.val);
            temp=temp.next;
        }
        arr.add(temp.val);
        Collections.sort(arr);

        ListNode ans=new ListNode();

        ListNode first=ans;
        ListNode before=first;
        for (int i=0;i<arr.size();i++){
            before=first;
            ListNode ansNext=new ListNode();
            first.val=arr.get(i);
            first.next=ansNext;

            first=first.next;
        }
        if(before!=null){
            before.next=null;
        }
        return  ans;
    }

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}

