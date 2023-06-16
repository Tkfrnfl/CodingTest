import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class comeBackHome {
    static int r,c,k;
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<String>[]arr;
    static ArrayList<Integer>[]visit;
    static int[]x={0,0,1,-1};
    static int[]y={1,-1,0,0};
    static int ans=0;
    public static void main()throws Exception {

        st=new StringTokenizer(br.readLine()," ");

        r=Integer.parseInt(st.nextToken());
        c=Integer.parseInt(st.nextToken());
        k=Integer.parseInt(st.nextToken());

        arr=new ArrayList[r];
        visit=new ArrayList[r];

        for(int i=0;i<r;i++){
            arr[i]=new ArrayList<>();
            visit[i]=new ArrayList<>();
        }
//        System.out.println(r);
//        System.out.println(arr);

        for(int i=0;i<r;i++){
            String str=br.readLine();
           // System.out.println(str);
            for(int j=0;j<c;j++){
                arr[i].add(String.valueOf( str.charAt(j)));
                visit[i].add(0);
           }
           // System.out.println(arr[i]);
        }

       // nul=visit;
        dfs(r-1,0,1);
        System.out.println(String.valueOf(ans));
    }
    public static void dfs(int a,int b,int length){

       // System.out.println(a+","+b+"/"+length);
        visit[a].set(b,1);
        for(int i=0;i<4;i++){
            int xx=a+x[i];
            int yy=b+y[i];

            if(length>k-1){
                toZero();
                return;
            }

            if(xx>=0 && xx<r &&yy>=0&&yy<c &&visit[xx].get(yy).equals(0) && arr[xx].get(yy).equals(".")){

                if(length==k-1 && xx==0 && yy== c-1){
                    toZero();
                    ans++;
                    return;
                }
                else if(length<k-1 && xx==0 && yy== c-1) {
                    toZero();
                    return;
                }
                else{
                    dfs(xx,yy,length+1);
                }
            }

            else if(xx<0 || xx>=r || yy<0 || yy>=c ) {
                continue;
            }
        }
        return;

    }
    public static void toZero(){
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                visit[i].set(j,0);
            }
        }
    }

}
