import java.util.Arrays;

// 스택을 직접 구현해보는 문제이다.
// 다른 자바 스택라이브러리를 제외하고 배열로만 구현해보았다.
// back 포인터로  pop,push등의 위치를 기억하였다.
public class minStack {
    public int min,front,back;

    public int[] stack=new int[60000];

    public MinStack() {             // 리트코드에서 minStack 을 직접 호출하므로 void 형식도 제거
        min=2147483647;
        front=0;
        back=0;
        Arrays.fill(stack,2147483647);
    }

    public void push(int val) {
        stack[back]=val;
        back++;
    }

    public void pop() {
        back--;
        //System.out.println(stack[back]);
        stack[back]=2147483647;
    }

    public int top() {
        back--;
        int re=stack[back];
        back++;
        return re;
    }

    public int getMin() {
        for(int i=front;i<=back;i++){
            min=Math.min(min,stack[i]);
        }
        int re = min;
        min=2147483647;
        return re;
    }
}
