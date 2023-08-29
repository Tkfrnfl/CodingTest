public class stackImpl {

    int top=0;
    int capacity=10000;

    Object[] stack =new Object[capacity];

    public void push(int val) {

        if (top>=capacity){                 //용량초과시 오버플로우
            System.out.println("overFlow");
            return;
        }
        stack[top]=val;
        top++;
    }

    public Object pop() {
        top--;
        Object re=stack[top];

        stack[top]=null;
        return re;
    }

    public Object peek() {

        int p=top-1;
        return stack[p];
    }
}
