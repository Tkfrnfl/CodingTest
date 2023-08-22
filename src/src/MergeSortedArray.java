import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        ArrayList<Integer> numArray1=new ArrayList<>();
        for (int i=0 ;i<m;i++) {numArray1.add(nums1[i]);}
        for (int i :nums2) numArray1.add(i);
        numArray1.sort(Comparator.naturalOrder());

        for(int i=0;i<m+n;i++){
            nums1[i]=numArray1.get(i);
        }
    }
}
