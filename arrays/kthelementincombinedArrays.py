def find_kth_element(nums1, nums2, k):
    def kth_helper(A, B, k):
        if not A:
            return B[k - 1]
        if not B:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        
        # Divide k into two halves
        idxA = min(len(A), k // 2)
        idxB = min(len(B), k // 2)
        
        if A[idxA - 1] <= B[idxB - 1]:
            # Exclude the first idxA elements of A
            return kth_helper(A[idxA:], B, k - idxA)
        else:
            # Exclude the first idxB elements of B
            return kth_helper(A, B[idxB:], k - idxB)
    
    return kth_helper(nums1, nums2, k)

# Example usage
nums1 = [2, 3, 6, 7, 9]
nums2 = [1, 4, 8, 10]
k = 5
print("The {}-th element is {}".format(k, find_kth_element(nums1, nums2, k)))
