import java.util.List;
import java.util.ArrayList;

class Solution {
    // Solution for LeetCode problem 4
    // Median of Two Sorted Arrays

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        List<Integer> sorted = merge(nums1, nums2);
        int sortedLength = sorted.size();
        
        if (sortedLength % 2 == 1) {
            return sorted.get(sortedLength / 2);
        } else {
            int midpoint = sortedLength / 2;
            return (sorted.get(midpoint - 1) + sorted.get(midpoint)) / 2.0;
        }
    }
    
    private List<Integer> merge(int[] list1, int[] list2) {
        List<Integer> combined = new ArrayList<>();
        int i = 0;
        int j = 0;
        
        while (i < list1.length && j < list2.length) {
            if (list1[i] < list2[j]) {
                combined.add(list1[i]);
                i++;
            } else {
                combined.add(list2[j]);
                j++;
            }
        }
        
        while (i < list1.length) {
            combined.add(list1[i]);
            i++;
        }
        
        while (j < list2.length) {
            combined.add(list2[j]);
            j++;
        }
        
        return combined;
    }
}