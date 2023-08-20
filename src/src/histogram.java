import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;
public class histogram {
    static int n;
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static long arr[];
    static Stack<Integer> stack = new Stack<Integer>();
    public static void main() throws Exception {

        st=new StringTokenizer(br.readLine());
        n= Integer.parseInt( st.nextToken());

        arr=new long[n];

        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            arr[i]=Integer.parseInt(st.nextToken());
        }


        long max=0;
        for(int i=0;i<n;i++){
            while ((!stack.isEmpty())&& arr[stack.peek()]>=arr[i]){
                long height=arr[stack.pop()];
                long width = stack.isEmpty() ? i : i - 1 - stack.peek();

                max=Math.max(max,height*width);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()){
            long height =arr[stack.pop()];
            long width=stack.isEmpty() ? n:n-1-stack.peek();
            max=Math.max(max,height*width);
        }


        System.out.println(max);

    }
}
