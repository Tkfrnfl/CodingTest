import java.util.HashMap;
import java.util.Map;

public class ransomNote {
    //주어진 두 문자열 ransomNote, magazine 에서 magazine의 철자조합으로 ransomNote을 만들수있는지 판단하는 문제이다.
    //magazine문자열을 순회하며 hash 테이블에 담고 ransomNote을 순회하며 hash테이블에 있는지 확인하였다.
    public boolean canConstruct(String ransomNote, String magazine) {
        boolean ans=true;
        Map<Character,Integer> table=new HashMap<>();
        for(int i=0;i<magazine.length();i++){
            if(table.get(magazine.charAt(i))==null) {               //처음에 테이블에 아예없을시 1저장
                table.put(magazine.charAt(i), 1);
            }
            else {
                table.put(magazine.charAt(i), table.get(magazine.charAt(i)) + 1); //있을시 +1저장
            }
        }
        for(int i=0;i<ransomNote.length();i++){
            if(table.get(ransomNote.charAt(i))==null||table.get(ransomNote.charAt(i))==0){
                return false;
            }
            else {
                table.put(ransomNote.charAt(i),table.get(ransomNote.charAt(i))-1);      //있을시 -1하여저장
            }
        }

        return ans;
    }
}
