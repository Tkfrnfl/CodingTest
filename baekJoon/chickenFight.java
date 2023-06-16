package baekJoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class chickenFight{

    int[] parent;
    public void main(String[] args)throws Exception {
        int n,m;

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n=Integer.parseInt(br.readLine());
        m=Integer.parseInt(br.readLine());

        ArrayList<Integer>[]arrE=new ArrayList[n+1];
        ArrayList<Integer>[]arrF=new ArrayList[n+1];
        parent=new int[n+1];

        for(int i=1;i<=n;i++){
            arrE[i]=new ArrayList<>();
            arrF[i]=new ArrayList<>();
            parent[i]=i;
        }
        for(int i=0;i<m;i++){
            st=new StringTokenizer(br.readLine());
            if(st.nextToken().equals("E")){
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arrE[a].add(b);
                arrE[b].add(a);
            }else {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arrF[a].add(b);
                arrF[b].add(a);
            }
        }

        for(int i=1;i<=n;i++){
            for(int j=0;j< arrE[i].size();j++){
                int tmp=arrE[i].get(j);
                for(int k=0;k<arrE[tmp].size();k++){
                    if(i==arrE[tmp].get(k)) continue;
                    arrF[i].add(arrE[tmp].get(k));
                    arrF[arrE[tmp].get(k)].add(i);
                }
            }
        }
        for(int i=1;i<n;i++){
            for(int j=0;j<arrF[i].size();j++){

            }
        }

    }
    public static void union(int a){

    }
    public static void union(int a,int b) {

    }
}