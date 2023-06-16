import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class comeBackHome {
    int r,c,k;
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    ArrayList<String>[]arr;
    ArrayList<Integer>[]visit;
    ArrayList<Integer>[]nul;
    int[]x={0,0,1,-1};
    int[]y={1,-1,0,0};
    int ans=0;
    public void main()throws Exception {

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
        System.out.println(r);
        System.out.println(arr);

        for(int i=0;i<r;i++){
//            st=new StringTokenizer(br.readLine());
//            String tmp=st.nextToken();
//            System.out.println(tmp);
//            arr[i].add(tmp);
            String str=br.readLine();
            System.out.println(str);
            for(int j=0;j<c;j++){
                arr[i].add(String.valueOf( str.charAt(j)));
                visit[i].add(0);
           }
            System.out.println(arr[i]);
        }

       // nul=visit;
        dfs(r-1,0,1);
        System.out.println(ans);
    }
    public void dfs(int a,int b,int length){

        System.out.println(a+","+b+"/"+length);
//        System.out.println(b);
//        System.out.println("----");
//        System.out.println(length);
//        System.out.println("----");
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
    public void toZero(){
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                visit[i].set(j,0);
            }
        }
    }

}
