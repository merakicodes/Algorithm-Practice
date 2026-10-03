#===============================================
#              BUBBLE SORT 
#===============================================

#Sorts a given array by bubble sort
#Input: An array A[0..n - 1] of orderable elements
#Output: Array A[0..n - 1] sorted in nondecreasing order

"""
What the Algorithm does:
A brute-force application to the sorting problem is to compare adjacent 
elements of the list and exchange them if they are out of order. By doing it
repeatedly, we end up "bubbling up" the largest element to the last position on
the list

"""

def bubble_sort(A):
 for i in range (len(A) - 1):
   for j in range (len(A) - 1):
    if A[j+1] < A[j]:
     A[j] , A[j+1] = A[j+1] , A[j]

 return A

A = [89, 45, 68, 90, 29, 34, 17]

print (bubble_sort(A))

