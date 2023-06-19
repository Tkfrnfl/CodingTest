import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
public class scale {
    static int n,m;
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<Integer>[][]arr;
    static int ans[][];
    static int answer[];

    public static void main() throws Exception{
        st=new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        m=Integer.parseInt(st.nextToken());

        arr=new ArrayList[n][2];
        ans=new int[n][n];
        answer=new int[n];

        for(int j=0;j<n;j++){
            for(int i=0;i<2;i++){
                arr[j][i]=new ArrayList<>();
            }
        }
        for(int i=0;i<n;i++){
            Arrays.fill(ans[i],0);
        }
        Arrays.fill(answer,0);



        //System.out.println(ans[0][0]);
        for(int i=0;i<m;i++){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            a-=1;
            b-=1;
            arr[a][1].add(b);
            arr[b][0].add(a);
        }
        for(int i=0;i<n;i++){
           dfsB(i,i);
           dfsS(i,i);
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j){
                    continue;
                }
                else if(ans[i][j]!=1) {
                    answer[i]++;
                }
            }

        }
        for(int i=0;i<n;i++){
            System.out.println(answer[i]);
        }


    }
    public static void dfsB(int a,int parent){
        if(arr[a][0].size()==0){
            return;
        }
        for (int i=0;i<arr[a][0].size();i++){
            if(ans[parent][arr[a][0].get(i)]==0){
                ans[parent][arr[a][0].get(i)]=1;
                dfsB(arr[a][0].get(i),parent);
            }
        }
    }
    public static void dfsS(int a,int parent){
        if(arr[a][1].size()==0){
            return;
        }
        for (int i=0;i<arr[a][1].size();i++){
            //System.out.println(String.valueOf(a)+"/"+String.valueOf(parent) );
            if(ans[parent][arr[a][1].get(i)]==0){
                ans[parent][arr[a][1].get(i)]=1;
                dfsS(arr[a][1].get(i),parent);
            }
        }
    }
}
