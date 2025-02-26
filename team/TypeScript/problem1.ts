function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    // Solution for LeetCode problem 4
    // Median of Two Sorted Arrays

    function merge(list1: number[], list2: number[]): number[] {
        let combined: number[] = []
        let i: number = 0
        let j: number = 0

        while ((i < list1.length) && (j < list2.length)) {
            if (list1[i] < list2[j]) {
                combined.push(list1[i])
                i += 1
            } else {
                combined.push(list2[j])
                j += 1
            }
        }

        while (i < list1.length) {
            combined.push(list1[i])
            i += 1
        }

        while (j < list2.length) {
            combined.push(list2[j])
            j += 1
        }

        return combined
    }

    let sorted: number[] = merge(nums1, nums2)
    let sorted_length: number = sorted.length

    if (sorted_length % 2 === 1){
        return sorted[Math.floor(sorted_length / 2)]
    } else {
        let midpoint: number = sorted_length / 2
        return (sorted[midpoint - 1] + sorted[midpoint]) / 2
    }
};